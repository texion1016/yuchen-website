import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const allowedOrigins = new Set([
  "https://yuchen-realty.com",
  "https://www.yuchen-realty.com",
]);

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
  if (!allowedOrigins.has(origin)) return response({ error: "Unapproved origin" }, 403, "https://yuchen-realty.com");
  if (request.method === "OPTIONS") return response(null, 204, origin);
  if (request.method !== "POST") return response({ error: "Method not allowed" }, 405, origin);

  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) return response({ error: "Authentication required" }, 401, origin);

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

  const { data: role, error: roleError } = await userClient.from("user_roles").select("role").eq("user_id", auth.user.id).maybeSingle();
  if (roleError) {
    console.error("Could not verify the caller's administrator role", roleError);
    return response({ error: "Could not verify administrator permission" }, 500, origin);
  }
  if (role?.role !== "admin") return response({ error: "Administrator permission required" }, 403, origin);

  let body: { email?: unknown; projects?: unknown };
  try { body = await request.json(); } catch { return response({ error: "Invalid request body" }, 400, origin); }
  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const projects = Array.isArray(body.projects)
    ? [...new Set(body.projects.filter((name): name is string => typeof name === "string").map((name) => name.trim()).filter(Boolean))]
    : [];
  if (!/^\S+@\S+\.\S+$/.test(email) || email.length > 254) return response({ error: "A valid email is required" }, 400, origin);
  if (!projects.length || projects.length > 30) return response({ error: "Assign at least one project" }, 400, origin);

  const { data: existingProjects, error: projectError } = await adminClient.from("projects").select("name").in("name", projects);
  if (projectError || (existingProjects?.length ?? 0) !== projects.length) return response({ error: "One or more project names are invalid" }, 400, origin);

  const { data: invited, error: inviteError } = await adminClient.auth.admin.inviteUserByEmail(email, { redirectTo: `${origin}/index.html` });
  if (inviteError || !invited.user) return response({ error: "This email may already have an account, or the invitation could not be sent" }, 400, origin);

  const { error: roleError } = await adminClient.from("user_roles").upsert({ user_id: invited.user.id, role: "builder" });
  if (roleError) return response({ error: "Could not grant builder access" }, 500, origin);

  const { error: assignmentError } = await adminClient.from("builder_projects").insert(projects.map((project_name) => ({ user_id: invited.user.id, project_name })));
  if (assignmentError) return response({ error: "Could not assign builder projects" }, 500, origin);

  return response({ message: "Builder invitation sent" }, 200, origin);
});
