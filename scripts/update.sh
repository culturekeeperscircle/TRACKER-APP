#!/bin/bash
# TCKC Threat Tracker - Quick Update Script
# Convenient wrapper for comprehensive_update.py with common options

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TRACKER_DIR="$(dirname "$SCRIPT_DIR")"
cd "$TRACKER_DIR"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_banner() {
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║  TCKC THREAT TRACKER - COMPREHENSIVE UPDATE AUTOMATION    ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_usage() {
    echo "Usage: ./update.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  (no args)      Interactive mode - prompts for confirmation"
    echo "  --auto         Fully automated - no prompts"
    echo "  --dry-run      Preview changes without committing"
    echo "  --help         Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./update.sh              # Interactive"
    echo "  ./update.sh --auto       # Automated"
    echo "  ./update.sh --dry-run    # Preview only"
}

check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
        exit 1
    fi
}

check_git() {
    if ! command -v git &> /dev/null; then
        echo -e "${RED}Error: Git is required but not installed.${NC}"
        exit 1
    fi
}

main() {
    print_banner
    
    # Check dependencies
    check_python
    check_git
    
    # Parse arguments
    case "${1:-}" in
        --help)
            print_usage
            exit 0
            ;;
        --auto)
            echo -e "${GREEN}Running in automatic mode...${NC}"
            python3 scripts/comprehensive_update.py --auto
            ;;
        --dry-run)
            echo -e "${YELLOW}Running in dry-run mode (no commits)...${NC}"
            python3 scripts/comprehensive_update.py --dry-run
            ;;
        "")
            echo -e "${BLUE}Interactive Mode${NC}"
            echo ""
            echo "This will:"
            echo "  1. Fetch latest from GitHub"
            echo "  2. Check for new entries"
            echo "  3. Integrate them into tracker"
            echo "  4. Commit and push to GitHub"
            echo ""
            read -p "Continue? (y/n): " -n 1 -r
            echo ""
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                python3 scripts/comprehensive_update.py
            else
                echo "Cancelled."
                exit 0
            fi
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            print_usage
            exit 1
            ;;
    esac
    
    # Check exit code
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓ Update completed successfully!${NC}"
        echo "Entries are now live on GitHub: https://github.com/culturekeeperscircle/TRACKER-APP"
    else
        echo ""
        echo -e "${RED}✗ Update failed. Check logs above.${NC}"
        exit 1
    fi
}

main "$@"
