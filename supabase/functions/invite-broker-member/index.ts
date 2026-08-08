import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set(["https://yuchen-realty.com", "https://www.yuchen-realty.com"]);
function apiKey(keysVariable: string, legacyVariable: string) {
  try { const keys = JSON.parse(Deno.env.get(keysVariable) ?? "{}"); if (typeof keys.default === "string" && keys.default) return keys.default; } catch { /* fallback */ }
  return Deno.env.get(legacyVariable) ?? "";
}
function reply(body: Record<string, string> | null, status: number, origin: string) {
  return new Response(body ? JSON.stringify(body) : null, { status, headers: {
    "Content-Type": "application/json", "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS", "Vary": "Origin",
  }});
}
function validEmail(value: string) { return /^\S+@\S+\.\S+$/.test(value) && value.length <= 254; }

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
  const { data: auth, error: authError } = await userClient.auth.getUser(authorization.slice(7));
  if (authError || !auth.user) return reply({ error: "Invalid session" }, 401, origin);
  const { data: caller } = await userClient.from("broker_company_members")
    .select("company_id, member_role, status")
    .eq("user_id", auth.user.id).maybeSingle();
  if (!caller || caller.status !== "active" || !["owner", "manager"].includes(caller.member_role)) return reply({ error: "Company manager permission required" }, 403, origin);

  let body: Record<string, unknown>;
  try { body = await request.json(); } catch { return reply({ error: "Invalid request body" }, 400, origin); }
  const name = typeof body.name === "string" ? body.name.trim() : "";
  const phone = typeof body.phone === "string" ? body.phone.trim() : "";
  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const licenseNo = typeof body.licenseNo === "string" ? body.licenseNo.trim() : "";
  const memberRole = body.memberRole === "manager" ? "manager" : "agent";
  if (!name || name.length > 100 || !phone || phone.length > 40 || !validEmail(email) || licenseNo.length > 80) return reply({ error: "Member information is incomplete" }, 400, origin);

  const { data: company } = await adminClient.from("broker_companies").select("display_name,status").eq("id", caller.company_id).maybeSingle();
  if (!company || company.status !== "active") return reply({ error: "Company information is unavailable" }, 500, origin);
  const { data: invited, error: inviteError } = await adminClient.auth.admin.inviteUserByEmail(email, {
    redirectTo: origin, data: { platform_invitation: "broker_company_member" },
  });
  if (inviteError || !invited.user) return reply({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);
  const rollbackUser = async () => { await adminClient.auth.admin.deleteUser(invited.user.id); };
  const { data: broker, error: brokerError } = await adminClient.from("brokers").insert({
    auth_user_id: invited.user.id, name, company: company.display_name, phone, email, license_no: licenseNo || null, status: "active",
  }).select("id").single();
  if (brokerError || !broker) { await rollbackUser(); return reply({ error: "Could not create member account" }, 500, origin); }
  const { error: membershipError } = await adminClient.from("broker_company_members").insert({
    company_id: caller.company_id, user_id: invited.user.id, broker_id: broker.id,
    member_role: memberRole, status: "active", invited_by: auth.user.id,
  });
  if (membershipError) {
    await adminClient.from("brokers").delete().eq("id", broker.id);
    await rollbackUser();
    return reply({ error: "Could not create company membership" }, 500, origin);
  }
  return reply({ message: "Member invitation sent" }, 200, origin);
});
