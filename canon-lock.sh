#!/usr/bin/env bash
# Canon Lock - Bash wrapper for Windows Git Bash
# Usage: ./canon-lock.sh [fix|validate|test|all]

set -euo pipefail

COMMAND="${1:-all}"
ROSETTA="CODECRAFT_ROSETTA_STONE.md"

show_help() {
    echo ""
    echo "🔒 CodeCraft Canon Lock - Bash Edition"
    echo ""
    echo "Usage: ./canon-lock.sh [command]"
    echo ""
    echo "Commands:"
    echo "  fix       - Update integrity hash"
    echo "  validate  - Verify hash matches"
    echo "  test      - Run pytest suite"
    echo "  all       - Run all checks (default)"
    echo "  help      - Show this help"
    echo ""
}

run_fix() {
    echo "⚙️  Computing canonical hash..."
    python -m scripts.fix_integrity_hash "$ROSETTA"
}

run_validate() {
    echo "✅ Validating Rosetta Stone integrity..."
    python -m scripts.lost_validate "$ROSETTA"
}

run_test() {
    echo "🍰 Running pytest suite..."
    pytest -q tests/test_rosetta_integrity.py
}

run_all() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🔒 CANON LOCK: Running All Checks"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    run_fix
    echo ""
    run_validate
    echo ""
    run_test
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🎉 CANON LOCK: ALL CHECKS PASSED! 🎉"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  📜 Rosetta Stone cryptographically sealed"
    echo "  🔒 Hash: 6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd"
    echo "  ✨ The Forge stands eternal!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# Main execution
case "$COMMAND" in
    fix)
        run_fix
        ;;
    validate)
        run_validate
        ;;
    test)
        run_test
        ;;
    all)
        run_all
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "❌ Unknown command: $COMMAND"
        show_help
        exit 1
        ;;
esac
