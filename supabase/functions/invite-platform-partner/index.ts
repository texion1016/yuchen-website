import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set(["https://yuchen-realty.com", "https://www.yuchen-realty.com"]);
const allowedRoles = new Set(["regional_agent", "sourcing_partner"]);

function apiKey(keysVariable: string, legacyVariable: string) {
  try {
    const keys = JSON.parse(Deno.env.get(keysVariable) ?? "{}");
    if (typeof keys.default === "string" && keys.default) return keys.default;
  } catch { /* legacy environment variables are supported below */ }
  return Deno.env.get(legacyVariable) ?? "";
}
function reply(body: Record<string, string> | null, status: number, origin: string) {
  return new Response(body ? JSON.stringify(body) : null, { status, headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  }});
}

Deno.serve(async (request) => {
  const origin = request.headers.get("origin") ?? "";
  if (!allowedOrigins.has(origin)) return reply({ error: "Unapproved origin" }, 403, "https://yuchen-realty.com");
  if (request.method === "OPTIONS") return reply(null, 204, origin);
  if (request.method !== "POST") return reply({ error: "Method not allowed" }, 405, origin);

  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) return reply({ error: "Authentication required" }, 401, origin);
  const url = Deno.env.get("SUPABASE_URL") ?? "";
  const publishableKey = apiKey("SUPABASE_PUBLISHABLE_KEYS", "SUPABASE_ANON_KEY");
  const serviceRoleKey = apiKey("SUPABASE_SECRET_KEYS", "SUPABASE_SERVICE_ROLE_KEY");
  if (!url || !publishableKey || !serviceRoleKey) return reply({ error: "Invitation service is not configured" }, 500, origin);

  const userClient = createClient(url, publishableKey, { global: { headers: { Authorization: authorization } }, auth: { autoRefreshToken: false, persistSession: false } });
  const adminClient = createClient(url, serviceRoleKey, { auth: { autoRefreshToken: false, persistSession: false } });
  const token = authorization.slice(7);
  const { data: auth, error: authError } = await userClient.auth.getUser(token);
  if (authError || !auth.user) return reply({ error: "Invalid session" }, 401, origin);
  const { data: role } = await userClient.from("user_roles").select("role").eq("user_id", auth.user.id).maybeSingle();
  if (role?.role !== "admin") return reply({ error: "Administrator permission required" }, 403, origin);

  let body: Record<string, unknown>;
  try { body = await request.json(); } catch { return reply({ error: "Invalid request body" }, 400, origin); }
  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const partnerRole = typeof body.role === "string" ? body.role.trim() : "";
  const displayName = typeof body.displayName === "string" ? body.displayName.trim() : "";
  const phone = typeof body.phone === "string" ? body.phone.trim() : "";
  const region = typeof body.region === "string" ? body.region.trim() : "";
  if (!/^\S+@\S+\.\S+$/.test(email) || email.length > 254 || !allowedRoles.has(partnerRole) || !displayName || displayName.length > 100 || phone.length > 40 || region.length > 100) {
    return reply({ error: "Partner information is incomplete or invalid" }, 400, origin);
  }
  if (partnerRole === "regional_agent" && !region) return reply({ error: "A regional agent must have a responsible region" }, 400, origin);

  // The console URL is already an allowed Supabase redirect URL. It forwards the
  // invitation callback to the correct partner portal before any admin UI loads.
  const { data: invited, error: inviteError } = await adminClient.auth.admin.inviteUserByEmail(email, {
    redirectTo: origin + "/yc-console-8k3n7q.html",
    data: { platform_invitation: partnerRole },
  });
  if (inviteError || !invited.user) return reply({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);

  const rollbackUser = async () => { await adminClient.auth.admin.deleteUser(invited.user.id); };
  const { error: roleError } = await adminClient.from("user_roles").upsert({ user_id: invited.user.id, role: partnerRole });
  if (roleError) { await rollbackUser(); return reply({ error: "Could not grant the partner role" }, 500, origin); }
  const { error: partnerError } = await adminClient.from("platform_partners").insert({
    user_id: invited.user.id, role: partnerRole, display_name: displayName,
    phone: phone || null, region: region || null, invited_by: auth.user.id,
  });
  if (partnerError) {
    await adminClient.from("user_roles").delete().eq("user_id", invited.user.id);
    await rollbackUser();
    return reply({ error: "Could not create the partner account" }, 500, origin);
  }
  return reply({ message: "Partner invitation sent" }, 200, origin);
});
