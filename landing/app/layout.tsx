import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'TCKC Threat Tracker',
  description:
    'Conversational interface for The Culture Keepers Circle Cultural Resource Threat Tracker.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-900 antialiased">{children}</body>
    </html>
  );
}
