/**
 * Profession taxonomy for the gate. Locked 2026-05-07.
 *
 * Edits land here. Changing this list does not require a schema migration;
 * `chat_sessions.profession` is a free-text column. Keep `value` stable so
 * historical analytics still group correctly.
 */

export type Profession = {
  value: string;
  label: string;
  description?: string;
};

export const PROFESSIONS: Profession[] = [
  { value: 'lawyer',           label: 'Lawyer / paralegal',                       description: 'Civil rights, immigration, environmental, tribal, etc.' },
  { value: 'journalist',       label: 'Journalist / writer' },
  { value: 'k12_educator',     label: 'K-12 educator / school staff' },
  { value: 'university',       label: 'University faculty / staff' },
  { value: 'museum_staff',     label: 'Museum / gallery staff' },
  { value: 'archivist',        label: 'Archivist / records professional' },
  { value: 'librarian',        label: 'Librarian / library staff' },
  { value: 'tribal_council',   label: 'Tribal council / Native nation government' },
  { value: 'ngo',              label: 'NGO / nonprofit / advocacy' },
  { value: 'federal_worker',   label: 'Federal employee or contractor' },
  { value: 'state_local',      label: 'State / local government' },
  { value: 'philanthropy',     label: 'Philanthropy / grantmaking' },
  { value: 'faith_leader',     label: 'Faith leader / faith community' },
  { value: 'artist_cultural',  label: 'Artist / cultural worker' },
  { value: 'healthcare',       label: 'Healthcare provider / public health' },
  { value: 'organizer',        label: 'Community organizer' },
  { value: 'student',          label: 'Student' },
  { value: 'retiree',          label: 'Retiree / private citizen' },
  { value: 'other',            label: 'Other (please specify)' },
];

export const isValidProfession = (value: string): boolean =>
  PROFESSIONS.some(p => p.value === value);
