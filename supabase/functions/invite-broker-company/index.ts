import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set(["https://yuchen-realty.com", "https://www.yuchen-realty.com"]);

function apiKey(keysVariable: string, legacyVariable: string) {
  try {
    const keys = JSON.parse(Deno.env.get(keysVariable) ?? "{}");
    if (typeof keys.default === "string" && keys.default) return keys.default;
  } catch { /* use the legacy variable below */ }
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

  const userClient = createClient(url, publishableKey, {
    global: { headers: { Authorization: authorization } },
    auth: { autoRefreshToken: false, persistSession: false },
  });
  const adminClient = createClient(url, serviceRoleKey, { auth: { autoRefreshToken: false, persistSession: false } });
  const token = authorization.slice(7);
  const { data: auth, error: authError } = await userClient.auth.getUser(token);
  if (authError || !auth.user) return reply({ error: "Invalid session" }, 401, origin);
  const { data: role } = await userClient.from("user_roles").select("role").eq("user_id", auth.user.id).maybeSingle();
  if (role?.role !== "admin") return reply({ error: "Administrator permission required" }, 403, origin);

  let body: Record<string, unknown>;
  try { body = await request.json(); } catch { return reply({ error: "Invalid request body" }, 400, origin); }
  const legalName = typeof body.legalName === "string" ? body.legalName.trim() : "";
  const displayName = typeof body.displayName === "string" ? body.displayName.trim() : legalName;
  const taxId = typeof body.taxId === "string" ? body.taxId.trim() : "";
  const ownerName = typeof body.ownerName === "string" ? body.ownerName.trim() : "";
  const ownerPhone = typeof body.ownerPhone === "string" ? body.ownerPhone.trim() : "";
  const ownerEmail = typeof body.ownerEmail === "string" ? body.ownerEmail.trim().toLowerCase() : "";
  if (!legalName || legalName.length > 150 || !displayName || displayName.length > 150 || !ownerName || ownerName.length > 100 || !ownerPhone || ownerPhone.length > 40 || !validEmail(ownerEmail) || taxId.length > 30) {
    return reply({ error: "Company and responsible-person information is incomplete" }, 400, origin);
  }

  const { data: invited, error: inviteError } = await adminClient.auth.admin.inviteUserByEmail(ownerEmail, {
    redirectTo: origin,
    data: { platform_invitation: "broker_company_owner" },
  });
  if (inviteError || !invited.user) return reply({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);

  const rollbackUser = async () => { await adminClient.auth.admin.deleteUser(invited.user.id); };
  const { data: company, error: companyError } = await adminClient.from("broker_companies").insert({
    legal_name: legalName, display_name: displayName, tax_id: taxId || null,
    contact_name: ownerName, contact_phone: ownerPhone, created_by: auth.user.id,
  }).select("id, display_name").single();
  if (companyError || !company) { await rollbackUser(); return reply({ error: "Could not create broker company" }, 500, origin); }

  const { data: broker, error: brokerError } = await adminClient.from("brokers").insert({
    auth_user_id: invited.user.id, name: ownerName, company: company.display_name,
    phone: ownerPhone, email: ownerEmail, status: "active",
  }).select("id").single();
  if (brokerError || !broker) {
    await adminClient.from("broker_companies").delete().eq("id", company.id);
    await rollbackUser();
    return reply({ error: "Could not create company owner account" }, 500, origin);
  }
  const { error: membershipError } = await adminClient.from("broker_company_members").insert({
    company_id: company.id, user_id: invited.user.id, broker_id: broker.id,
    member_role: "owner", status: "active", invited_by: auth.user.id,
  });
  if (membershipError) {
    await adminClient.from("brokers").delete().eq("id", broker.id);
    await adminClient.from("broker_companies").delete().eq("id", company.id);
    await rollbackUser();
    return reply({ error: "Could not create company membership" }, 500, origin);
  }
  return reply({ message: "Broker company invitation sent" }, 200, origin);
});
