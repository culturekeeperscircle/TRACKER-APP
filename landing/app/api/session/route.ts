/**
 * POST /api/session
 *
 * Creates a chat_sessions row from the gate form. Sets a session-id cookie.
 * Returns the session id so the client can include it in chat requests.
 *
 * Anonymity contract: we accept profession, profession_other (when "other"),
 * state_code, and zip5. We hash a short prefix of the User-Agent header so we
 * have a coarse abuse-detection signal; we do not store the raw UA, the IP,
 * or any other identifier.
 */
import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';
import crypto from 'node:crypto';
import { requireServerSupabase } from '@/lib/supabase';
import { isValidProfession } from '@/lib/professions';
import { isValidState } from '@/lib/states';

const schema = z.object({
  profession: z.string().min(1),
  profession_other: z.string().optional(),
  state_code: z.string().min(2).max(5),
  zip5: z.string().regex(/^\d{5}$/).optional(),
});

export const runtime = 'nodejs';

export async function POST(req: NextRequest) {
  let body: unknown;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: 'invalid_json' }, { status: 400 });
  }

  const parsed = schema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: 'invalid_input', details: parsed.error.issues }, { status: 400 });
  }
  const { profession, profession_other, state_code, zip5 } = parsed.data;

  if (!isValidProfession(profession)) {
    return NextResponse.json({ error: 'unknown_profession' }, { status: 400 });
  }
  if (!isValidState(state_code)) {
    return NextResponse.json({ error: 'unknown_state' }, { status: 400 });
  }
  if (profession === 'other' && (!profession_other || profession_other.length < 2)) {
    return NextResponse.json({ error: 'profession_other_required' }, { status: 400 });
  }

  // Coarse UA hash for abuse detection only. Not an identifier.
  const ua = req.headers.get('user-agent') ?? '';
  const ua_hash = crypto.createHash('sha256').update(ua).digest('hex').slice(0, 16);

  const supabase = requireServerSupabase();
  const { data, error } = await supabase
    .from('chat_sessions')
    .insert({
      profession,
      profession_other: profession === 'other' ? profession_other : null,
      state_code,
      zip5: zip5 ?? null,
      user_agent_hash: ua_hash,
    })
    .select('id')
    .single();

  if (error || !data) {
    console.error('session insert error:', error);
    return NextResponse.json({ error: 'session_create_failed' }, { status: 500 });
  }

  const res = NextResponse.json({ session_id: data.id });
  res.cookies.set('tckc_sid', data.id, {
    httpOnly: true,
    secure: true,
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 30, // 30 days
  });
  return res;
}
