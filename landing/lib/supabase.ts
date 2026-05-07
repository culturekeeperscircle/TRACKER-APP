/**
 * Supabase clients.
 *
 * - `serverSupabase`: service-role client for the API routes. Server-only.
 *   Bypasses RLS so the chat backend can read the entries table and write to
 *   chat_sessions / chat_turns.
 * - No browser-side client is exposed; the gate and chat both go through API
 *   routes. Keeps the service role key off the wire.
 */
import { createClient } from '@supabase/supabase-js';

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!url) {
  throw new Error('NEXT_PUBLIC_SUPABASE_URL not set');
}

export const serverSupabase = serviceRoleKey
  ? createClient(url, serviceRoleKey, {
      auth: { persistSession: false, autoRefreshToken: false },
    })
  : null;

export function requireServerSupabase() {
  if (!serverSupabase) {
    throw new Error('SUPABASE_SERVICE_ROLE_KEY not set; server cannot read entries.');
  }
  return serverSupabase;
}
