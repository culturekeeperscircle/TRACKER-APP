"""
Shared Supabase HTTP client for the TCKC pipeline.

Authentication precedence:
  1. SUPABASE_SERVICE_ROLE_KEY (preferred — bypasses RLS, the canonical key
     for server-side automation and the GitHub Actions workflow).
  2. SUPABASE_ANON_KEY (works only when a permissive policy is open;
     used for local one-off loads).

Project ref defaults to xsqdjhjcqbawghuaqqwj. Override with SUPABASE_PROJECT_REF.
"""
import os
import sys

DEFAULT_PROJECT_REF = "xsqdjhjcqbawghuaqqwj"


def get_credentials():
    project_ref = os.environ.get("SUPABASE_PROJECT_REF", DEFAULT_PROJECT_REF)
    service_role = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    anon = os.environ.get("SUPABASE_ANON_KEY")

    if service_role:
        key, kind = service_role, "service_role"
    elif anon:
        key, kind = anon, "anon"
    else:
        sys.stderr.write(
            "Neither SUPABASE_SERVICE_ROLE_KEY nor SUPABASE_ANON_KEY is set.\n"
            "Service role is required for the GitHub Actions workflow.\n"
            "Find the service role key under Studio → Settings → API.\n"
        )
        sys.exit(2)

    base_url = f"https://{project_ref}.supabase.co/rest/v1"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    return {
        "project_ref": project_ref,
        "base_url": base_url,
        "key_kind": kind,
        "headers": headers,
    }
