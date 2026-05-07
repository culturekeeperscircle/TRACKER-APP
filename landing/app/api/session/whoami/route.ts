/**
 * GET /api/session/whoami
 *
 * Returns 200 if the tckc_sid cookie maps to a real chat_sessions row,
 * 401 otherwise. Used by the landing page to decide between Gate and Chat.
 */
import { NextRequest, NextResponse } from 'next/server';
import { requireServerSupabase } from '@/lib/supabase';

export const runtime = 'nodejs';

export async function GET(req: NextRequest) {
  const sid = req.cookies.get('tckc_sid')?.value;
  if (!sid) {
    return NextResponse.json({ error: 'no_cookie' }, { status: 401 });
  }
  const supabase = requireServerSupabase();
  const { data, error } = await supabase
    .from('chat_sessions')
    .select('id')
    .eq('id', sid)
    .single();
  if (error || !data) {
    return NextResponse.json({ error: 'unknown_session' }, { status: 401 });
  }
  return NextResponse.json({ session_id: data.id });
}
