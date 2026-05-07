'use client';

/**
 * Chat surface. Uses the Vercel AI SDK's useChat hook.
 * Streams the assistant response, renders message list, exposes pills.
 */
import { useChat } from 'ai/react';
import TopicPills from './TopicPills';

export default function Chat() {
  const { messages, input, setInput, handleSubmit, isLoading } = useChat({
    api: '/api/chat',
  });

  return (
    <div className="mx-auto flex max-w-3xl flex-col gap-3 p-4">
      <header className="border-b pb-3">
        <h1 className="text-xl font-semibold">TCKC Threat Tracker</h1>
        <p className="text-xs text-gray-600">
          Ask about federal actions affecting Indigenous, African-descendant, Latine,
          Asian, and Pacific Islander cultural resources. Sources cited inline.
        </p>
      </header>

      <ol className="space-y-4">
        {messages.map((m) => (
          <li key={m.id}>
            <div className="mb-1 text-xs font-semibold uppercase tracking-wider text-gray-500">
              {m.role === 'user' ? 'You' : 'Tracker'}
            </div>
            <div className="whitespace-pre-wrap text-sm text-gray-900">{m.content}</div>
          </li>
        ))}
      </ol>

      {messages.length === 0 && <TopicPills onPick={(q) => setInput(q)} />}

      <form onSubmit={handleSubmit} className="sticky bottom-0 flex gap-2 border-t bg-white pt-3">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about federal actions affecting cultural resources..."
          className="flex-1 rounded border border-gray-300 px-3 py-2"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="rounded bg-black px-4 py-2 text-white disabled:bg-gray-300"
        >
          {isLoading ? 'Thinking...' : 'Ask'}
        </button>
      </form>

      <footer className="border-t pt-3 text-xs text-gray-500">
        Informational summary, not legal advice.{' '}
        <a href="https://www.culturekeeperscircle.org/tracker" className="underline">
          Browse all entries
        </a>
        .
      </footer>
    </div>
  );
}
