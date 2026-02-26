"""Validate Google Form entry IDs match what's in index.html.

Fetches each Google Form page, extracts actual entry IDs from the HTML,
and compares them to the IDs hardcoded in index.html. Fails with exit
code 1 if any mismatch is found.

Run: python scripts/validate_forms.py
"""
import re
import sys
import requests

# ── Forms and their expected entry IDs (from index.html) ──────────────
FORMS = {
    'Gate (TCKC Access)': {
        'url': 'https://docs.google.com/forms/d/e/1FAIpQLScHEjRatYzgLqrEPvfo8ICutIQWIIpJ06WZtB6xd_0BUQrAaw/viewform',
        'expected_ids': ['756520214', '1031550334'],
    },
    'Analytics (Session Summary)': {
        'url': 'https://docs.google.com/forms/d/e/1FAIpQLSc6gpcwZB07jlUt9dmaspmjjt9UoqRctQaVABeitP1L03eILw/viewform',
        'expected_ids': ['1251519131', '1838122374', '979202646', '1389873863', '1953500271'],
    },
    'Flag (Issue Reporting)': {
        'url': 'https://docs.google.com/forms/d/e/1FAIpQLSeiqdC_XFdFYPG4XVwV0nJW5oQ4FPcgoVhntDTUXDi5WWW1zA/viewform',
        'expected_ids': ['1357684968', '448582309', '677931112'],
    },
}


def get_form_entry_ids(url):
    """Fetch a Google Form page and extract all entry IDs from the HTML."""
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    # Google Forms embed entry IDs in multiple patterns
    ids = set()
    for match in re.findall(r'\[(\d{6,12}),', resp.text):
        ids.add(match)
    for match in re.findall(r'entry\.(\d{6,12})', resp.text):
        ids.add(match)
    return ids


def validate():
    all_ok = True
    for name, form in FORMS.items():
        print(f'\n── {name} ──')
        print(f'   URL: {form["url"]}')
        try:
            actual_ids = get_form_entry_ids(form['url'])
        except Exception as e:
            print(f'   ERROR: Could not fetch form: {e}')
            all_ok = False
            continue

        missing = []
        for expected_id in form['expected_ids']:
            if expected_id in actual_ids:
                print(f'   ✓ entry.{expected_id} — found')
            else:
                print(f'   ✗ entry.{expected_id} — NOT FOUND in form HTML')
                missing.append(expected_id)

        if missing:
            all_ok = False
            print(f'   ⚠ MISMATCH: {len(missing)} entry ID(s) not found!')
            print(f'   Actual IDs found in form: {sorted(actual_ids)}')
        else:
            print(f'   All {len(form["expected_ids"])} entry IDs verified ✓')

    return all_ok


if __name__ == '__main__':
    print('Google Form Entry ID Validator')
    print('=' * 50)
    ok = validate()
    print('\n' + '=' * 50)
    if ok:
        print('ALL FORMS VALIDATED SUCCESSFULLY')
        sys.exit(0)
    else:
        print('VALIDATION FAILED — entry IDs need updating in index.html')
        sys.exit(1)
