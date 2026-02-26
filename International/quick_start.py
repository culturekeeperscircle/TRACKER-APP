#!/usr/bin/env python3
"""
================================================================================
QUICK START - International Obligations Data Extractor
================================================================================

Run this script to immediately start pulling data from all sources.

Usage:
    python quick_start.py              # Extract from all free sources
    python quick_start.py --full       # Extract from all sources (needs WTO key)
    python quick_start.py --export     # Extract and export for Threat Tracker

Requirements:
    pip install requests beautifulsoup4

Optional (for WTO trade data):
    export WTO_API_KEY="your-api-key"
================================================================================
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from master_extractor import MasterExtractor, ExtractorConfig


def quick_extract(full: bool = False, export: bool = False):
    """
    Quick extraction with minimal configuration.
    
    Args:
        full: If True, includes WTO (requires API key)
        export: If True, exports data for Threat Tracker
    """
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║           INTERNATIONAL OBLIGATIONS DATA EXTRACTOR                           ║
║                    Quick Start Mode                                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Data Sources:                                                               ║
║  • WTO   - World Trade Organization (disputes, trade data)                   ║
║  • IMF   - International Monetary Fund (economic indicators)                 ║
║  • WB    - World Bank (development indicators)                               ║
║  • UN    - United Nations (Security Council resolutions)                     ║
║  • ICJ   - International Court of Justice (cases)                            ║
║  • NATO  - North Atlantic Treaty Organization (communiqués)                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Check for dependencies
    try:
        import requests
    except ImportError:
        print("ERROR: 'requests' library not installed.")
        print("Install with: pip install requests")
        sys.exit(1)
    
    # Configure
    config = ExtractorConfig()
    
    # Check WTO API key
    wto_key = os.getenv('WTO_API_KEY')
    if wto_key:
        config.wto_api_key = wto_key
        print("✓ WTO API key found")
    else:
        print("⚠ WTO API key not set - trade data will be limited")
        print("  Set with: export WTO_API_KEY='your-key'")
        print("  Get key from: https://apiportal.wto.org/")
    
    print()
    
    # Determine sources
    if full:
        sources = ['wto', 'imf', 'world_bank', 'un', 'icj', 'nato']
    else:
        # Free sources that don't require API keys
        sources = ['imf', 'world_bank', 'un', 'icj']
        if wto_key:
            sources.insert(0, 'wto')
    
    print(f"Extracting from: {', '.join(s.upper() for s in sources)}")
    print("-" * 70)
    
    # Initialize and extract
    extractor = MasterExtractor(config)
    results = extractor.extract_all(sources)
    
    # Summary
    print("\n" + "=" * 70)
    print("EXTRACTION COMPLETE")
    print("=" * 70)
    
    total = 0
    for source, result in results.items():
        records = result.get('records', 0)
        total += records
        status = "✓" if 'error' not in result else "✗"
        print(f"  {status} {source.upper():15} {records:>6} records")
    
    print("-" * 70)
    print(f"    {'TOTAL':15} {total:>6} records")
    print()
    
    # Export if requested
    if export:
        output_path = './exports/threat_tracker_data.json'
        extractor.export_for_threat_tracker(output_path)
        print(f"✓ Exported to: {output_path}")
    
    # Show what's available
    print("\nData stored in: ./data/intl_obligations.db")
    print("\nQuick queries you can run:")
    print("  - US-involved ICJ cases")
    print("  - UNSC resolutions mentioning cultural heritage")
    print("  - Economic indicators affecting funding")
    print("  - WTO disputes involving cultural goods")
    
    return extractor


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Quick Start Data Extraction')
    parser.add_argument('--full', action='store_true', 
                        help='Include all sources (WTO requires API key)')
    parser.add_argument('--export', action='store_true',
                        help='Export data for Threat Tracker')
    
    args = parser.parse_args()
    
    extractor = quick_extract(full=args.full, export=args.export)
    
    # Interactive mode hint
    print("\n" + "-" * 70)
    print("For more options, run: python master_extractor.py --help")
    print("-" * 70)


if __name__ == '__main__':
    main()
