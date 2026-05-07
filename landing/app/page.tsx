'use client';

import { useEffect, useState } from 'react';
import Gate from '@/components/Gate';
import Chat from '@/components/Chat';

export default function HomePage() {
  const [ready, setReady] = useState<boolean | null>(null);

  useEffect(() => {
    // Probe the cookie; if a session exists, skip the gate.
    fetch('/api/session/whoami', { credentials: 'include' })
      .then((r) => setReady(r.ok))
      .catch(() => setReady(false));
  }, []);

  if (ready === null) {
    return <main className="p-8 text-sm text-gray-500">Loading...</main>;
  }
  return <main>{ready ? <Chat /> : <Gate onReady={() => setReady(true)} />}</main>;
}
