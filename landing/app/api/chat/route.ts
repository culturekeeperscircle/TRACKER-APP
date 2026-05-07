/**
 * POST /api/chat
 *
 * Body: { messages: [{ role, content }, ...] }
 *
 * Flow:
 *   1. Read tckc_sid cookie; look up the chat_sessions row.
 *   2. Take the last user message; retrieve top 8 entries via full-text search.
 *   3. If retrieval is empty, log a refusal turn and return the canned refusal
 *      ("I do not see this in the tracker"). No Claude call.
 *   4. Otherwise, build the system prompt with the retrieved entries, call
 *      Claude Sonnet 4.6 via the Vercel AI SDK with streaming on.
 *   5. After the stream finishes, write the user turn and the assistant turn
 *      to chat_turns with retrieved_ids populated.
 *
 * Rate limiting hook: see TODO at the top of the handler. The cleanest place
 * is in middleware.ts; this route assumes that has run.
 */
import { NextRequest } from 'next/server';
import { anthropic } from '@ai-sdk/anthropic';
import { streamText } from 'ai';
import { requireServerSupabase } from '@/lib/supabase';
import { retrieve } from '@/lib/retrieval';
import { buildSystemPrompt, REFUSAL_NO_RETRIEVAL } from '@/lib/system-prompt';
import { PROFESSIONS } from '@/lib/professions';
import { STATES } from '@/lib/states';

export const runtime = 'nodejs';
export const maxDuration = 60;  // seconds

type Msg = { role: 'user' | 'assistant' | 'system'; content: string };

function lookupLabel(value: string, list: { value?: string; code?: string; label?: string; name?: string }[]): string {
  const hit = list.find((x) => (x as any).value === value || (x as any).code === value);
  return hit ? (hit as any).label ?? (hit as any).name ?? value : value;
}

export async function POST(req: NextRequest) {
  // TODO(rate-limit): per-session and per-IP token-bucket. Move to middleware
  // once the abuse profile is observed.
  const sid = req.cookies.get('tckc_sid')?.value;
  if (!sid) {
    return new Response(JSON.stringify({ error: 'no_session' }), {
      status: 401, headers: { 'content-type': 'application/json' },
    });
  }

  const supabase = requireServerSupabase();
  const { data: session, error: sessErr } = await supabase
    .from('chat_sessions')
    .select('id, profession, profession_other, state_code')
    .eq('id', sid)
    .single();
  if (sessErr || !session) {
    return new Response(JSON.stringify({ error: 'session_not_found' }), {
      status: 401, headers: { 'content-type': 'application/json' },
    });
  }

  const body = await req.json();
  const messages: Msg[] = Array.isArray(body?.messages) ? body.messages : [];
  const lastUser = [...messages].reverse().find((m) => m.role === 'user');
  if (!lastUser) {
    return new Response(JSON.stringify({ error: 'no_user_message' }), { status: 400 });
  }

  const retrieved = await retrieve(lastUser.content, 8);

  // Refusal path: no retrieval = no answer.
  if (retrieved.length === 0) {
    await supabase.from('chat_turns').insert([
      { session_id: sid, role: 'user',      content: lastUser.content, retrieved_ids: [] },
      {
        session_id: sid, role: 'assistant', content: REFUSAL_NO_RETRIEVAL,
        retrieved_ids: [], refused: true, refusal_reason: 'no_retrieval',
      },
    ]);
    return new Response(REFUSAL_NO_RETRIEVAL, {
      status: 200, headers: { 'content-type': 'text/plain; charset=utf-8' },
    });
  }

  const professionLabel = session.profession === 'other'
    ? (session.profession_other ?? 'private citizen')
    : lookupLabel(session.profession, PROFESSIONS as any);
  const stateName = lookupLabel(session.state_code, STATES as any);
  const systemPrompt = buildSystemPrompt({
    professionLabel,
    stateName,
    retrievedEntries: retrieved,
  });
  const retrievedIds = retrieved.map((r) => r.id);

  // Always log the user turn before streaming. The assistant turn is written
  // in the onFinish callback below so we capture the full content + token count.
  await supabase.from('chat_turns').insert({
    session_id: sid,
    role: 'user',
    content: lastUser.content,
    retrieved_ids: retrievedIds,
  });

  const result = streamText({
    model: anthropic('claude-sonnet-4-6'),
    system: systemPrompt,
    messages: messages.filter((m) => m.role !== 'system') as any,
    temperature: 0.2,
    maxTokens: 1500,
    onFinish: async ({ text, usage }) => {
      try {
        await supabase.from('chat_turns').insert({
          session_id: sid,
          role: 'assistant',
          content: text,
          retrieved_ids: retrievedIds,
          tokens_in: usage?.promptTokens,
          tokens_out: usage?.completionTokens,
        });
        await supabase
          .from('chat_sessions')
          .update({ last_seen_at: new Date().toISOString() })
          .eq('id', sid);
      } catch (e) {
        console.error('chat_turns assistant insert failed:', e);
      }
    },
  });

  return result.toDataStreamResponse();
}
