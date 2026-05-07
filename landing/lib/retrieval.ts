/**
 * Retrieval over the entries table. Phase 1 uses Postgres full-text search via
 * the existing entries_fts_idx. Phase 3 will add pgvector embeddings for
 * hybrid retrieval; the function signature here is stable across phases.
 */
import { requireServerSupabase } from './supabase';

export type RetrievedEntry = {
  id: string;
  official_name: string | null;
  severity: string | null;
  action_date: string | null;
  administration: string | null;
  agencies: string[];
  summary: string | null;
  description_text: string;
  source_url: string | null;
};

const MAX_DESCRIPTION_CHARS = 1500;

function stripHtml(s: string | null): string {
  if (!s) return '';
  return s.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
}

export async function retrieve(query: string, k: number = 8): Promise<RetrievedEntry[]> {
  const supabase = requireServerSupabase();

  // PostgREST cannot run plainto_tsquery directly via the JS client; use the
  // built-in textSearch wrapper, which targets `description_html`. The existing
  // entries_fts_idx is on a tsvector built from official_name + summary +
  // description_html, so we issue a parallel filter on official_name and
  // summary as a safety net.
  const { data, error } = await supabase
    .from('entries')
    .select('id, official_name, severity, action_date, administration, agencies, summary, description_html, source_url')
    .or(`description_html.plfts.${query},official_name.plfts.${query},summary.plfts.${query}`)
    .order('action_date', { ascending: false, nullsFirst: false })
    .limit(k);

  if (error) {
    console.error('retrieve error:', error);
    return [];
  }

  return (data ?? []).map((row: any) => ({
    id: row.id,
    official_name: row.official_name,
    severity: row.severity,
    action_date: row.action_date,
    administration: row.administration,
    agencies: row.agencies ?? [],
    summary: row.summary,
    description_text: stripHtml(row.description_html).slice(0, MAX_DESCRIPTION_CHARS),
    source_url: row.source_url,
  }));
}
