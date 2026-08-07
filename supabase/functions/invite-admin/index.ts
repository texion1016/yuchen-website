import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set([
  "https://yuchen-realty.com",
  "https://www.yuchen-realty.com",
]);

function apiKey(keysVariable: string, legacyVariable: string) {
  try {
    const keys = JSON.parse(Deno.env.get(keysVariable) ?? "{}");
    if (typeof keys.default === "string" && keys.default) return keys.default;
  } catch {
    // Fall back to the legacy environment variable below.
  }
  return Deno.env.get(legacyVariable) ?? "";
}

function adminApiHeaders(key: string) {
  const headers: Record<string, string> = {
    "apikey": key,
    "Content-Type": "application/json",
  };
  if (!key.startsWith("sb_secret_")) {
    headers.Authorization = `Bearer ${key}`;
  }
  return headers;
}

function response(body: Record<string, string> | null, status: number, origin: string) {
  return new Response(body ? JSON.stringify(body) : null, {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Vary": "Origin",
    },
  });
}

Deno.serve(async (request) => {
  const origin = request.headers.get("origin") ?? "";
  if (!allowedOrigins.has(origin)) {
    return response({ error: "Unapproved origin" }, 403, "https://yuchen-realty.com");
  }
  if (request.method === "OPTIONS") return response(null, 204, origin);
  if (request.method !== "POST") return response({ error: "Method not allowed" }, 405, origin);

  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) {
    return response({ error: "Authentication required" }, 401, origin);
  }

  const url = Deno.env.get("SUPABASE_URL") ?? "";
  const publishableKey = apiKey("SUPABASE_PUBLISHABLE_KEYS", "SUPABASE_ANON_KEY");
  const serviceRoleKey = apiKey("SUPABASE_SECRET_KEYS", "SUPABASE_SERVICE_ROLE_KEY");
  if (!publishableKey || !serviceRoleKey) {
    return response({ error: "Invitation service is not configured" }, 500, origin);
  }
  const userClient = createClient(url, publishableKey, {
    global: { headers: { Authorization: authorization } },
    auth: { autoRefreshToken: false, persistSession: false },
  });
  const token = authorization.slice("Bearer ".length);
  const { data: auth, error: authError } = await userClient.auth.getUser(token);
  if (authError || !auth.user) return response({ error: "Invalid session" }, 401, origin);

  const { data: role, error: roleError } = await userClient
    .from("user_roles")
    .select("role")
    .eq("user_id", auth.user.id)
    .maybeSingle();
  if (roleError) {
    console.error("Could not verify the caller's administrator role", roleError);
    return response({ error: "Could not verify administrator permission" }, 500, origin);
  }
  if (role?.role !== "admin") {
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

  const adminHeaders = adminApiHeaders(serviceRoleKey);
  const invitationResponse = await fetch(`${url}/rest/v1/rpc/create_admin_invitation`, {
    method: "POST",
    headers: adminHeaders,
    body: JSON.stringify({
      invitation_email: email,
      invitation_invited_by: auth.user.id,
      invitation_expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
    }),
  });
  if (!invitationResponse.ok) {
    console.error("Could not create admin invitation record", invitationResponse.status, await invitationResponse.text());
    return response({ error: "Could not create invitation" }, 500, origin);
  }

  const inviteResponse = await fetch(`${url}/auth/v1/invite`, {
    method: "POST",
    headers: adminHeaders,
    body: JSON.stringify({ email, redirect_to: `${origin}/yc-console-8k3n7q.html` }),
  });
  if (!inviteResponse.ok) {
    console.error("Could not send administrator invitation", inviteResponse.status, await inviteResponse.text());
    await fetch(`${url}/rest/v1/rpc/delete_pending_admin_invitation`, {
      method: "POST",
      headers: adminHeaders,
      body: JSON.stringify({ invitation_email: email }),
    });
    return response({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);
  }

  return response({ message: "Invitation sent" }, 200, origin);
});
