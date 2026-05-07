'use client';

/**
 * Curated starter prompts. Click a pill to fill the chat input.
 * Edits land here. Pills should be short and ask about specific
 * federal actions or agencies the tracker covers.
 */
const PILLS = [
  'What did the GSA POST API removal change about public comment?',
  'Which Smithsonian programming changes are tracked since January 2025?',
  'Show me Trump II actions affecting tribal consultation.',
  'What is in the tracker about NEA grant rescissions?',
  'How has DEI rescission affected federal cultural agencies?',
  'What immigration enforcement actions affect Latine communities?',
  'List SEVERE actions from this month.',
  'What does the tracker say about birthright citizenship litigation?',
  'How many actions hit HBCU funding?',
  'What changed at IMLS under Trump II?',
  'What is the status of NAGPRA regulatory amendments?',
  'Summarize federal court decisions on DACA since 2025.',
];

export default function TopicPills({ onPick }: { onPick: (q: string) => void }) {
  return (
    <div className="flex flex-wrap gap-2 px-2 py-3">
      {PILLS.map((p) => (
        <button
          key={p}
          type="button"
          onClick={() => onPick(p)}
          className="rounded-full border border-gray-300 px-3 py-1 text-sm text-gray-700 hover:border-gray-500"
        >
          {p}
        </button>
      ))}
    </div>
  );
}
