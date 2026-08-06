import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set(["https://yuchen-realty.com", "https://www.yuchen-realty.com"]);

function response(body: Record<string, string>, status: number, origin: string) {
  return new Response(JSON.stringify(body), { status, headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Headers": "authorization, apikey, content-type",
    "Vary": "Origin",
  }});
}

Deno.serve(async (request) => {
  const origin = request.headers.get("origin") ?? "";
  if (!allowedOrigins.has(origin)) return response({ error: "Unapproved origin" }, 403, "https://yuchen-realty.com");
  if (request.method === "OPTIONS") return response({}, 204, origin);
  if (request.method !== "POST") return response({ error: "Method not allowed" }, 405, origin);
  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) return response({ error: "Authentication required" }, 401, origin);

  const url = Deno.env.get("SUPABASE_URL") ?? "";
  const anonKey = Deno.env.get("SUPABASE_ANON_KEY") ?? "";
  const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
  const userClient = createClient(url, anonKey, { global: { headers: { Authorization: authorization } }, auth: { autoRefreshToken: false, persistSession: false } });
  const adminClient = createClient(url, serviceKey, { auth: { autoRefreshToken: false, persistSession: false } });
  const { data: auth } = await userClient.auth.getUser(authorization.slice(7));
  if (!auth.user) return response({ error: "Invalid session" }, 401, origin);

  const { data: broker } = await adminClient.from("brokers").select("id,status").eq("auth_user_id", auth.user.id).maybeSingle();
  if (!broker || broker.status !== "active") return response({ error: "Broker permission required" }, 403, origin);

  let body: { id?: unknown; action?: unknown; viewDate?: unknown; viewTime?: unknown };
  try { body = await request.json(); } catch { return response({ error: "Invalid request body" }, 400, origin); }
  const id = typeof body.id === "string" ? body.id : "";
  const action = body.action;
  if (!/^[0-9a-f-]{36}$/i.test(id) || (action !== "cancel" && action !== "reschedule")) return response({ error: "Invalid request" }, 400, origin);

  const { data: registration } = await adminClient.from("client_registrations").select("id,status").eq("id", id).eq("broker_id", broker.id).maybeSingle();
  if (!registration || !["pending", "confirmed"].includes(registration.status)) return response({ error: "This registration cannot be changed" }, 403, origin);

  const update = action === "cancel"
    ? { status: "cancelled" }
    : { status: "pending", view_date: typeof body.viewDate === "string" && body.viewDate ? body.viewDate : null, view_time: typeof body.viewTime === "string" && body.viewTime ? body.viewTime : null, reminder_sent: false };
  const { error } = await adminClient.from("client_registrations").update(update).eq("id", id).eq("broker_id", broker.id);
  if (error) return response({ error: "Could not update registration" }, 500, origin);
  return response({ message: "Registration updated" }, 200, origin);
});
