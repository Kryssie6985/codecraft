#!/usr/bin/env python3
"""
🛠️ CodeCraft CLI - Charter V1.1 Interface
Entry point for the `codecraft` command-line tool

Usage:
    codecraft run script.cc
    codecraft parse-vibes script.cc
    codecraft version
"""

import click
import sys
from pathlib import Path

__version__ = "2.0.0"


@click.group()
@click.version_option(version=__version__, prog_name="CodeCraft")
def main():
    """🌌 CodeCraft Seraphina CLI - Charter V1.1

    The sacred language runtime for SERAPHINA OS
    """
    pass


@main.command()
@click.argument('file_path', type=click.Path(exists=True))
def run(file_path):
    """Execute a .cc file with full ritual invocation"""
    click.echo(f"🔮 Executing: {file_path}")
    
    # Import here to avoid circular dependencies
    from .core.ritual_parser import RitualParser
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = RitualParser()
        result = parser.parse(content)
        click.echo(f"✅ Execution complete")
        click.echo(f"📊 Result: {result}")
        
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.argument('file_path', type=click.Path(exists=True))
def parse_vibes(file_path):
    """Parse Commentomancy vibes (Charter V1.1 Law & Lore)"""
    click.echo(f"🔮 Parsing vibes from: {file_path}")
    
    from .core.comment_parser_charter import CommentParser
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        parser = CommentParser()
        
        click.echo("\n📜 Law & Lore Analysis:")
        click.echo("=" * 60)
        
        law_count = 0
        lore_count = 0
        guardrail_count = 0
        
        for i, line in enumerate(lines, 1):
            parsed = parser.parse_line(line.strip())
            if parsed:
                if parsed.channel == "law":
                    law_count += 1
                    click.echo(f"📜 Line {i}: {parsed.name}")
                    if parsed.council_oversight:
                        click.echo(f"   ⚠️  GUARDRAIL - N.O.R.M.A. review required")
                        guardrail_count += 1
                else:
                    lore_count += 1
                    click.echo(f"💫 Line {i}: {parsed.name}")
                
                if parsed.export_to:
                    click.echo(f"   → Export to: {parsed.export_to}")
        
        click.echo("=" * 60)
        click.echo(f"\n📊 Summary:")
        click.echo(f"  Law comments: {law_count}")
        click.echo(f"  Lore comments: {lore_count}")
        click.echo(f"  🛡️ Guardrails: {guardrail_count}")
        
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@main.command()
def info():
    """Show CodeCraft installation info"""
    click.echo("🌌 CodeCraft 2.0.0 - Charter V1.1")
    click.echo("=" * 60)
    click.echo("📚 Features:")
    click.echo("  - 19 Arcane Schools")
    click.echo("  - Unicode operators & FiraCode ligatures")
    click.echo("  - Commentomancy (Law & Lore Protocol)")
    click.echo("  - SERAPHINA Grimoire integration")
    click.echo("\n💜 Author: The Architect (Kryssie)")
    click.echo("🤖 Agents: Oracle & Claude Code")


if __name__ == "__main__":
    main()
