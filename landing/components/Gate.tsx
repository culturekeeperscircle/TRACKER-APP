'use client';

/**
 * Gate component. Two questions, then unlock the chat. No email, no name,
 * no IP, no fingerprint.
 */
import { useState } from 'react';
import { PROFESSIONS } from '@/lib/professions';
import { STATES } from '@/lib/states';

export default function Gate({ onReady }: { onReady: () => void }) {
  const [profession, setProfession] = useState('');
  const [other, setOther] = useState('');
  const [stateCode, setStateCode] = useState('');
  const [zip, setZip] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  const valid =
    profession &&
    stateCode &&
    (profession !== 'other' || other.trim().length >= 2) &&
    (zip === '' || /^\d{5}$/.test(zip));

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    if (!valid || submitting) return;
    setSubmitting(true);
    setErr(null);
    try {
      const r = await fetch('/api/session', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({
          profession,
          profession_other: profession === 'other' ? other.trim() : undefined,
          state_code: stateCode,
          zip5: zip || undefined,
        }),
      });
      if (!r.ok) {
        const j = await r.json().catch(() => ({}));
        throw new Error(j.error ?? 'session_failed');
      }
      onReady();
    } catch (e: any) {
      setErr(e.message ?? 'failed');
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={submit} className="mx-auto max-w-xl space-y-6 p-6">
      <header className="space-y-2">
        <h1 className="text-2xl font-semibold">The Culture Keepers Circle Threat Tracker</h1>
        <p className="text-sm text-gray-600">
          Two answers and we will personalize a briefing on what is hitting your
          industry. We do not store your name, email, or IP address.
        </p>
      </header>

      <fieldset className="space-y-2">
        <label htmlFor="profession" className="block text-sm font-medium">
          What best describes your work?
        </label>
        <select
          id="profession"
          required
          value={profession}
          onChange={(e) => setProfession(e.target.value)}
          className="w-full rounded border border-gray-300 px-3 py-2"
        >
          <option value="">Select...</option>
          {PROFESSIONS.map((p) => (
            <option key={p.value} value={p.value}>{p.label}</option>
          ))}
        </select>
        {profession === 'other' && (
          <input
            type="text"
            placeholder="Briefly describe your work"
            value={other}
            onChange={(e) => setOther(e.target.value)}
            className="w-full rounded border border-gray-300 px-3 py-2"
            maxLength={80}
          />
        )}
      </fieldset>

      <fieldset className="grid grid-cols-3 gap-3">
        <div className="col-span-2 space-y-2">
          <label htmlFor="state" className="block text-sm font-medium">State</label>
          <select
            id="state"
            required
            value={stateCode}
            onChange={(e) => setStateCode(e.target.value)}
            className="w-full rounded border border-gray-300 px-3 py-2"
          >
            <option value="">Select...</option>
            {STATES.map((s) => (
              <option key={s.code} value={s.code}>{s.name}</option>
            ))}
          </select>
        </div>
        <div className="space-y-2">
          <label htmlFor="zip" className="block text-sm font-medium">ZIP (optional)</label>
          <input
            id="zip"
            type="text"
            inputMode="numeric"
            pattern="\d{5}"
            placeholder="00000"
            value={zip}
            onChange={(e) => setZip(e.target.value.replace(/\D/g, '').slice(0, 5))}
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>
      </fieldset>

      {err && <p className="text-sm text-red-600">{err}</p>}

      <div className="flex items-center justify-between">
        <a
          href="https://www.culturekeeperscircle.org/tracker"
          className="text-sm text-gray-600 underline"
        >
          Skip and browse all entries
        </a>
        <button
          type="submit"
          disabled={!valid || submitting}
          className="rounded bg-black px-4 py-2 text-white disabled:bg-gray-300"
        >
          {submitting ? 'Loading...' : 'Start'}
        </button>
      </div>

      <footer className="border-t pt-4 text-xs text-gray-500">
        This tool summarizes federal actions tracked by The Culture Keepers Circle
        and is informational only. It is not legal advice.
      </footer>
    </form>
  );
}
