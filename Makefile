.PHONY: fix validate test all clean

fix:
	@echo "⚙️  Computing canonical hash..."
	@python -m scripts.fix_integrity_hash CODECRAFT_ROSETTA_STONE.md

validate:
	@echo "✅ Validating Rosetta Stone integrity..."
	@python -m scripts.lost_validate CODECRAFT_ROSETTA_STONE.md

test:
	@echo "🍰 Running pytest suite..."
	@pytest -q tests/test_rosetta_integrity.py

all: fix validate test
	@echo "🎉 Canon Lock: ALL CHECKS PASSED!"

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "🧹 Cleaned Python cache files"

help:
	@echo "CodeCraft Rosetta Stone - Canon Lock Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  make fix        - Update integrity hash"
	@echo "  make validate   - Verify hash matches"
	@echo "  make test       - Run pytest suite"
	@echo "  make all        - Run all checks (fix + validate + test)"
	@echo "  make clean      - Remove Python cache files"
	@echo "  make help       - Show this help"
