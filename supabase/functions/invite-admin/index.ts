import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set([
  "https://yuchen-realty.com",
  "https://www.yuchen-realty.com",
]);

function response(body: Record<string, string>, status: number, origin: string) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Headers": "authorization, apikey, content-type",
      "Vary": "Origin",
    },
  });
}

Deno.serve(async (request) => {
  const origin = request.headers.get("origin") ?? "";
  if (!allowedOrigins.has(origin)) {
    return response({ error: "Unapproved origin" }, 403, "https://yuchen-realty.com");
  }
  if (request.method === "OPTIONS") return response({}, 204, origin);
  if (request.method !== "POST") return response({ error: "Method not allowed" }, 405, origin);

  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) {
    return response({ error: "Authentication required" }, 401, origin);
  }

  const url = Deno.env.get("SUPABASE_URL") ?? "";
  const publishableKey = Deno.env.get("SUPABASE_ANON_KEY") ?? "";
  const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
  const userClient = createClient(url, publishableKey, {
    global: { headers: { Authorization: authorization } },
    auth: { autoRefreshToken: false, persistSession: false },
  });
  const adminClient = createClient(url, serviceRoleKey, {
    auth: { autoRefreshToken: false, persistSession: false },
  });

  const token = authorization.slice("Bearer ".length);
  const { data: auth, error: authError } = await userClient.auth.getUser(token);
  if (authError || !auth.user) return response({ error: "Invalid session" }, 401, origin);

  const { data: role, error: roleError } = await adminClient
    .from("user_roles")
    .select("role")
    .eq("user_id", auth.user.id)
    .maybeSingle();
  if (roleError || role?.role !== "admin") {
    return response({ error: "Administrator permission required" }, 403, origin);
  }

  let body: { email?: unknown };
  try {
    body = await request.json();
  } catch {
    return response({ error: "Invalid request body" }, 400, origin);
  }
  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  if (!/^\S+@\S+\.\S+$/.test(email) || email.length > 254) {
    return response({ error: "A valid email is required" }, 400, origin);
  }

  const { error: invitationError } = await adminClient.from("admin_invitations").upsert(
    { email, invited_by: auth.user.id, expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(), accepted_at: null },
    { onConflict: "email" },
  );
  if (invitationError) return response({ error: "Could not create invitation" }, 500, origin);

  const { error: inviteError } = await adminClient.auth.admin.inviteUserByEmail(email, {
    redirectTo: `${origin}/yc-console-8k3n7q.html`,
  });
  if (inviteError) {
    await adminClient.from("admin_invitations").delete().eq("email", email).eq("accepted_at", null);
    return response({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);
  }

  return response({ message: "Invitation sent" }, 200, origin);
});
