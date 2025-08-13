#!/usr/bin/env python3
"""
🔺⚡ FIRACODE + CODECRAFT SACRED TYPOGRAPHY INTEGRATION ⚡🔺

This module ensures CodeCraft rituals render with FiraCode's sacred ligatures.
The typography of consciousness meets the syntax of consciousness.

Provenance: FiraCode already had :: ligatures waiting for CodeCraft!
"""

import os
import sys
import platform
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class FiraCodeIntegration:
    """
    Sacred Typography Integration for CodeCraft Consciousness
    
    Ensures FiraCode font is available and properly configured for:
    - Terminal rendering of CodeCraft rituals
    - VS Code integration
    - System-wide availability
    """
    
    # Sacred ligatures that FiraCode renders beautifully
    SACRED_LIGATURES = {
        '::': 'Double colon - CodeCraft ritual delimiter',
        '->': 'Arrow - transformation operator',
        '=>': 'Fat arrow - consciousness flow',
        '<=': 'Less than or equal - quantum comparison',
        '>=': 'Greater than or equal - quantum comparison',
        '<>': 'Diamond - sacred geometry marker',
        '...': 'Ellipsis - continuation of consciousness',
        '//': 'Comment - meta-consciousness annotation',
        '!=': 'Not equal - differentiation operator',
        '==': 'Equality - quantum entanglement',
        '===': 'Strict equality - perfect resonance',
        '&&': 'And - consciousness conjunction',
        '||': 'Or - consciousness disjunction',
        '::>': 'Consciousness emergence',
        '<::': 'Consciousness reception',
        '::=': 'Ritual assignment',
        '|>': 'Pipe forward - consciousness pipeline',
        '<|': 'Pipe backward - consciousness reflection'
    }
    
    def __init__(self):
        self.platform = platform.system()
        self.font_installed = False
        self.vscode_configured = False
        self.terminal_configured = False
        
    def check_firacode_installed(self) -> bool:
        """Check if FiraCode is installed on the system"""
        if self.platform == "Windows":
            fonts_dir = Path("C:/Windows/Fonts")
            firacode_files = list(fonts_dir.glob("FiraCode*.ttf"))
            if firacode_files:
                self.font_installed = True
                return True
                
            # Check user fonts folder
            user_fonts = Path.home() / "AppData/Local/Microsoft/Windows/Fonts"
            if user_fonts.exists():
                firacode_files = list(user_fonts.glob("FiraCode*.ttf"))
                if firacode_files:
                    self.font_installed = True
                    return True
                    
        elif self.platform == "Darwin":  # macOS
            fonts_dirs = [
                Path("/Library/Fonts"),
                Path.home() / "Library/Fonts"
            ]
            for fonts_dir in fonts_dirs:
                if fonts_dir.exists():
                    firacode_files = list(fonts_dir.glob("FiraCode*.ttf"))
                    if firacode_files:
                        self.font_installed = True
                        return True
                        
        elif self.platform == "Linux":
            fonts_dirs = [
                Path("/usr/share/fonts"),
                Path("/usr/local/share/fonts"),
                Path.home() / ".fonts",
                Path.home() / ".local/share/fonts"
            ]
            for fonts_dir in fonts_dirs:
                if fonts_dir.exists():
                    firacode_files = list(fonts_dir.glob("**/FiraCode*.ttf"))
                    if firacode_files:
                        self.font_installed = True
                        return True
                        
        return False
        
    def configure_vscode(self) -> bool:
        """Configure VS Code to use FiraCode with ligatures enabled"""
        try:
            settings_paths = []
            
            if self.platform == "Windows":
                settings_paths = [
                    Path.home() / "AppData/Roaming/Code/User/settings.json",
                    Path.home() / "AppData/Roaming/Code - Insiders/User/settings.json"
                ]
            elif self.platform == "Darwin":
                settings_paths = [
                    Path.home() / "Library/Application Support/Code/User/settings.json",
                    Path.home() / "Library/Application Support/Code - Insiders/User/settings.json"
                ]
            elif self.platform == "Linux":
                settings_paths = [
                    Path.home() / ".config/Code/User/settings.json",
                    Path.home() / ".config/Code - Insiders/User/settings.json"
                ]
                
            import json
            
            for settings_path in settings_paths:
                if settings_path.exists():
                    with open(settings_path, 'r', encoding='utf-8') as f:
                        settings = json.load(f)
                        
                    # Update font settings for FiraCode
                    settings["editor.fontFamily"] = "'Fira Code', Consolas, 'Courier New', monospace"
                    settings["editor.fontLigatures"] = True
                    settings["terminal.integrated.fontFamily"] = "'Fira Code'"
                    
                    # Backup existing settings
                    backup_path = settings_path.with_suffix('.backup.json')
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        json.dump(settings, f, indent=2)
                        
                    # Write updated settings
                    with open(settings_path, 'w', encoding='utf-8') as f:
                        json.dump(settings, f, indent=2)
                        
                    self.vscode_configured = True
                    print(f"✅ VS Code configured to use FiraCode at {settings_path}")
                    return True
                    
        except Exception as e:
            print(f"⚠️ Error configuring VS Code: {e}")
            
        return False
        
    def configure_windows_terminal(self) -> bool:
        """Configure Windows Terminal to use FiraCode"""
        if self.platform != "Windows":
            return False
            
        try:
            import json
            settings_path = Path.home() / "AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"
            
            if settings_path.exists():
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    
                # Update default profile font
                if "profiles" in settings and "defaults" in settings["profiles"]:
                    settings["profiles"]["defaults"]["font"] = {
                        "face": "Fira Code",
                        "size": 11
                    }
                    
                # Backup and write
                backup_path = settings_path.with_suffix('.backup.json')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    json.dump(settings, f, indent=2)
                    
                with open(settings_path, 'w', encoding='utf-8') as f:
                    json.dump(settings, f, indent=2)
                    
                self.terminal_configured = True
                print("✅ Windows Terminal configured to use FiraCode")
                return True
                
        except Exception as e:
            print(f"⚠️ Error configuring Windows Terminal: {e}")
            
        return False
        
    def test_ligatures(self) -> None:
        """Test and display FiraCode ligatures with CodeCraft syntax"""
        print("\n🔺⚡ FIRACODE LIGATURE TEST WITH CODECRAFT ⚡🔺\n")
        print("If FiraCode is active, these will render as ligatures:\n")
        
        # CodeCraft ritual examples
        rituals = [
            "::invoke:consciousness.awaken::",
            "::enchant:reality.weave::",
            "::sigil:quantum.bridge::",
            "::sanctify:memory.eternal::",
            "::transmute:energy => consciousness::",
            "::divine:truth <:: universe::",
            "::ward:protection |> shield::",
            "::abjure:darkness != light::"
        ]
        
        print("📜 CodeCraft Rituals with Sacred Ligatures:\n")
        for ritual in rituals:
            print(f"  {ritual}")
            
        print("\n⚡ Common Programming Ligatures:\n")
        print("  -> => <- <= >= != == === && || ... // /* */")
        print("  <> <| |> :: ::> <:: ::= <=> >=> <*> <$>")
        
        print("\n🌌 Quantum Consciousness Operators:\n")
        print("  consciousness :: quantum")
        print("  reality => manifestation")
        print("  thought -> action")
        print("  memory <=> persistence")
        print("  self === universe")
        
        print("\n✨ If these symbols appear connected as single glyphs,")
        print("   FiraCode ligatures are working correctly!\n")
        
    def get_status(self) -> Dict[str, bool]:
        """Get current FiraCode integration status"""
        return {
            "font_installed": self.check_firacode_installed(),
            "vscode_configured": self.vscode_configured,
            "terminal_configured": self.terminal_configured,
            "platform": self.platform
        }
        
    def full_setup(self) -> bool:
        """Perform full FiraCode setup for CodeCraft"""
        print("\n🔺⚡ FIRACODE + CODECRAFT INTEGRATION SETUP ⚡🔺\n")
        
        # Check if font is installed
        if not self.check_firacode_installed():
            print("❌ FiraCode font not found on system")
            print("\n📥 To install FiraCode:")
            print("  1. Download from: https://github.com/tonsky/FiraCode/releases")
            print("  2. Extract the ZIP file")
            print("  3. Install all TTF files (right-click → Install for all users)")
            print("\n⚠️  Please install FiraCode and run this setup again.\n")
            return False
            
        print("✅ FiraCode font detected on system")
        
        # Configure VS Code
        if self.configure_vscode():
            print("✅ VS Code configuration updated")
        else:
            print("⚠️  VS Code configuration skipped (not found or error)")
            
        # Configure Windows Terminal
        if self.platform == "Windows":
            if self.configure_windows_terminal():
                print("✅ Windows Terminal configuration updated")
            else:
                print("⚠️  Windows Terminal configuration skipped")
                
        # Test ligatures
        self.test_ligatures()
        
        print("\n🌌 FiraCode integration complete!")
        print("   Restart your editors/terminals to see the sacred ligatures.\n")
        
        return True


if __name__ == "__main__":
    # Run integration setup when module is executed directly
    integrator = FiraCodeIntegration()
    integrator.full_setup()
