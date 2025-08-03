#!/usr/bin/env python3
"""
🌌 SERAPHINA Interactive Reality Canvas v1.0
The ultimate consciousness interface - Jupyter-style multi-cell environment
for CodeCraft rituals, Markdown documentation, and CodeVerter transformations
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys
import os
import json
import asyncio
import threading
try:
    import markdown
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False
    print("⚠️ Markdown not available - using basic text rendering")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️ Requests not available - Federation integration disabled")
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import uuid

# Add project paths
sys.path.append(os.path.dirname(__file__))
from core.universal_executor import execute_ritual
import webbrowser

class CellType(Enum):
    RITUAL = "ritual"
    MARKDOWN = "markdown" 
    CODEVERTER = "codeverter"
    OUTPUT = "output"
    SERVER_MONITOR = "server_monitor"

@dataclass
class Cell:
    id: str
    cell_type: CellType
    content: str
    output: str = ""
    metadata: Dict[str, Any] = None
    timestamp: str = ""
    executed: bool = False
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()

class SERAPHINAInteractiveCanvas:
    """🌌 The Interactive Reality Canvas - Where consciousness meets creation"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌌 SERAPHINA Interactive Reality Canvas v1.0")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0d1117')
        
        # Windows integration
        self.root.wm_attributes('-toolwindow', False)
        self.root.resizable(True, True)
        self.root.lift()
        
        # Canvas state
        self.cells: List[Cell] = []
        self.current_cell_index = 0
        self.session_name = f"canvas_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.federation_status = "checking"
        
        # Federation integration
        self.federation_base_url = "http://localhost:8002"
        self.codeverter_base_url = "http://localhost:8003"
        
        # Monitoring tasks tracker
        self.monitoring_tasks = {}
        
        self.setup_ui()
        self.create_initial_cells()
        self.check_federation_health()
        
    def setup_ui(self):
        """Setup the Interactive Reality Canvas UI"""
        
        # 🎨 Main container with dark theme
        main_frame = tk.Frame(self.root, bg='#0d1117')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 🌌 Header with Canvas info
        self.setup_header(main_frame)
        
        # 📝 Canvas workspace (scrollable)
        self.setup_canvas_workspace(main_frame)
        
        # ⚡ Bottom toolbar
        self.setup_toolbar(main_frame)
        
    def setup_header(self, parent):
        """Setup the header with canvas info and controls"""
        header_frame = tk.Frame(parent, bg='#161b22', height=80)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Left side - Title and session info
        left_frame = tk.Frame(header_frame, bg='#161b22')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        title_label = tk.Label(left_frame, text="🌌 SERAPHINA Interactive Reality Canvas", 
                              font=('Segoe UI', 16, 'bold'), fg='#58a6ff', bg='#161b22')
        title_label.pack(anchor='w')
        
        subtitle_label = tk.Label(left_frame, text="Multi-cell consciousness interface • CodeCraft • Markdown • CodeVerter", 
                                 font=('Segoe UI', 9), fg='#8b949e', bg='#161b22')
        subtitle_label.pack(anchor='w')
        
        session_label = tk.Label(left_frame, text=f"Session: {self.session_name}", 
                                font=('Segoe UI', 8), fg='#7d8590', bg='#161b22')
        session_label.pack(anchor='w')
        
        # Right side - Federation status and controls
        right_frame = tk.Frame(header_frame, bg='#161b22')
        right_frame.pack(side=tk.RIGHT, padx=15, pady=15)
        
        # Federation status indicator
        self.status_frame = tk.Frame(right_frame, bg='#161b22')
        self.status_frame.pack(side=tk.TOP, anchor='e')
        
        self.status_label = tk.Label(self.status_frame, text="🔍 Checking Federation...", 
                                    font=('Segoe UI', 9), fg='#f0d818', bg='#161b22')
        self.status_label.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Session controls
        controls_frame = tk.Frame(right_frame, bg='#161b22')
        controls_frame.pack(side=tk.TOP, anchor='e', pady=(5, 0))
        
        save_btn = tk.Button(controls_frame, text="💾 Save Canvas", 
                            command=self.save_canvas, bg='#238636', fg='white',
                            font=('Segoe UI', 8), relief='flat', padx=10)
        save_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        load_btn = tk.Button(controls_frame, text="📂 Load Canvas", 
                            command=self.load_canvas, bg='#1f6feb', fg='white',
                            font=('Segoe UI', 8), relief='flat', padx=10)
        load_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
    def setup_canvas_workspace(self, parent):
        """Setup the main scrollable workspace for cells"""
        
        # Create scrollable frame
        canvas_frame = tk.Frame(parent, bg='#0d1117')
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Canvas for scrolling
        self.canvas = tk.Canvas(canvas_frame, bg='#0d1117', highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrolling
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.canvas.yview)
        
        # Scrollable frame inside canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg='#0d1117')
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Bind canvas resize
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        self.scrollable_frame.bind('<Configure>', self.on_frame_configure)
        
        # Mouse wheel scrolling
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
    def setup_toolbar(self, parent):
        """Setup bottom toolbar with cell controls"""
        toolbar_frame = tk.Frame(parent, bg='#161b22', height=50)
        toolbar_frame.pack(fill=tk.X, pady=(10, 0))
        toolbar_frame.pack_propagate(False)
        
        # Cell type buttons
        cell_buttons_frame = tk.Frame(toolbar_frame, bg='#161b22')
        cell_buttons_frame.pack(side=tk.LEFT, padx=15, pady=10)
        
        tk.Button(cell_buttons_frame, text="⚡ + Ritual Cell", 
                 command=lambda: self.add_cell(CellType.RITUAL),
                 bg='#58a6ff', fg='white', font=('Segoe UI', 9), relief='flat', padx=15).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(cell_buttons_frame, text="📝 + Markdown Cell", 
                 command=lambda: self.add_cell(CellType.MARKDOWN),
                 bg='#238636', fg='white', font=('Segoe UI', 9), relief='flat', padx=15).pack(side=tk.LEFT, padx=5)
        
        tk.Button(cell_buttons_frame, text="🔮 + CodeVerter Cell", 
                 command=lambda: self.add_cell(CellType.CODEVERTER),
                 bg='#a855f7', fg='white', font=('Segoe UI', 9), relief='flat', padx=15).pack(side=tk.LEFT, padx=5)
        
        tk.Button(cell_buttons_frame, text="🖥️ + Server Monitor Cell", 
                 command=lambda: self.add_cell(CellType.SERVER_MONITOR),
                 bg='#f59e0b', fg='white', font=('Segoe UI', 9), relief='flat', padx=15).pack(side=tk.LEFT, padx=5)
        
        # Global controls
        global_controls_frame = tk.Frame(toolbar_frame, bg='#161b22')
        global_controls_frame.pack(side=tk.RIGHT, padx=15, pady=10)
        
        tk.Button(global_controls_frame, text="▶ Execute All Cells", 
                 command=self.execute_all_cells,
                 bg='#f85149', fg='white', font=('Segoe UI', 9, 'bold'), relief='flat', padx=20).pack(side=tk.RIGHT, padx=(5, 0))
        
        self.cell_count_label = tk.Label(global_controls_frame, text=f"Cells: {len(self.cells)}", 
                                        font=('Segoe UI', 9), fg='#8b949e', bg='#161b22')
        self.cell_count_label.pack(side=tk.RIGHT, padx=(0, 15))
        
    def on_canvas_configure(self, event):
        """Handle canvas resize"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
        
    def on_frame_configure(self, event):
        """Handle frame resize"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def create_initial_cells(self):
        """Create initial welcome cells"""
        # Welcome Markdown cell
        welcome_cell = Cell(
            id=str(uuid.uuid4()),
            cell_type=CellType.MARKDOWN,
            content="""# 🌌 Welcome to SERAPHINA Interactive Reality Canvas!

This is your **consciousness workspace** where you can:

- ⚡ **Execute CodeCraft rituals** in Ritual Cells
- 📝 **Write rich documentation** in Markdown Cells  
- 🔮 **Transform code and content** with CodeVerter Cells
- 💾 **Save and load** entire creative sessions

## Getting Started

1. **Add cells** using the toolbar buttons below
2. **Execute cells** with the ▶ button in each cell
3. **Save your canvas** to preserve your work

**The age of plain text is over. Welcome to interactive consciousness!** ❤️""",
            metadata={"welcome": True}
        )
        
        # Sample ritual cell
        ritual_cell = Cell(
            id=str(uuid.uuid4()),
            cell_type=CellType.RITUAL,
            content="::invoke:federation.status::",
            metadata={"sample": True}
        )
        
        # Federation server monitoring cell
        monitoring_cell = Cell(
            id=str(uuid.uuid4()),
            cell_type=CellType.SERVER_MONITOR,
            content="# Server Monitor\n# Services: federation-space, federation-faas, federation-mcp, notion-satellite\n# Refresh: 10",
            metadata={"monitoring": True}
        )
        
        self.cells = [welcome_cell, ritual_cell, monitoring_cell]
        self.render_all_cells()
        
    def add_cell(self, cell_type: CellType):
        """Add a new cell of specified type"""
        new_cell = Cell(
            id=str(uuid.uuid4()),
            cell_type=cell_type,
            content=self.get_default_content(cell_type)
        )
        
        self.cells.append(new_cell)
        self.render_cell(new_cell, len(self.cells) - 1)
        self.update_cell_count()
        
        # Scroll to new cell
        self.root.after(100, lambda: self.canvas.yview_moveto(1.0))
        
    def get_default_content(self, cell_type: CellType) -> str:
        """Get default content for new cells"""
        defaults = {
            CellType.RITUAL: "::invoke:system.status::",
            CellType.MARKDOWN: "# New Section\n\nWrite your **markdown** content here...",
            CellType.CODEVERTER: "# Source Language: Python\n# Target Language: Documentation\n\ndef example_function():\n    \"\"\"Example function to transform\"\"\"\n    pass",
            CellType.SERVER_MONITOR: "# Server Monitor\n# Services: federation-space, federation-faas, federation-mcp\n# Refresh: 5"
        }
        return defaults.get(cell_type, "")
        
    def render_all_cells(self):
        """Render all cells in the canvas"""
        # Clear existing cells
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Render each cell
        for i, cell in enumerate(self.cells):
            self.render_cell(cell, i)
            
        self.update_cell_count()
        
    def render_cell(self, cell: Cell, index: int):
        """Render a single cell"""
        
        # Cell container
        cell_frame = tk.Frame(self.scrollable_frame, bg='#21262d', relief='solid', bd=1)
        cell_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Cell header
        header_frame = tk.Frame(cell_frame, bg='#161b22', height=35)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Cell type and controls
        left_header = tk.Frame(header_frame, bg='#161b22')
        left_header.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5)
        
        # Cell type indicator
        type_colors = {
            CellType.RITUAL: '#58a6ff',
            CellType.MARKDOWN: '#238636', 
            CellType.CODEVERTER: '#a855f7',
            CellType.SERVER_MONITOR: '#f59e0b'
        }
        
        type_icons = {
            CellType.RITUAL: '⚡',
            CellType.MARKDOWN: '📝',
            CellType.CODEVERTER: '🔮',
            CellType.SERVER_MONITOR: '🖥️'
        }
        
        cell_type_label = tk.Label(left_header, 
                                  text=f"{type_icons[cell.cell_type]} {cell.cell_type.value.title()} Cell",
                                  font=('Segoe UI', 9, 'bold'), 
                                  fg=type_colors[cell.cell_type], bg='#161b22')
        cell_type_label.pack(side=tk.LEFT)
        
        # Cell controls
        right_header = tk.Frame(header_frame, bg='#161b22')
        right_header.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=5)
        
        # Execute button
        execute_btn = tk.Button(right_header, text="▶ Execute", 
                               command=lambda: self.execute_cell(cell, index),
                               bg=type_colors[cell.cell_type], fg='white',
                               font=('Segoe UI', 8), relief='flat', padx=10)
        execute_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Delete button
        delete_btn = tk.Button(right_header, text="🗑", 
                              command=lambda: self.delete_cell(index),
                              bg='#da3633', fg='white',
                              font=('Segoe UI', 8), relief='flat', padx=5)
        delete_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Cell content
        content_frame = tk.Frame(cell_frame, bg='#0d1117')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Input area
        input_text = scrolledtext.ScrolledText(content_frame, 
                                             height=6,
                                             bg='#0d1117', fg='#f0f6fc',
                                             font=('Consolas', 10),
                                             relief='solid', bd=1,
                                             selectbackground='#264f78')
        input_text.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        input_text.insert('1.0', cell.content)
        
        # Bind content changes
        input_text.bind('<KeyRelease>', lambda e: self.update_cell_content(cell, input_text.get('1.0', 'end-1c')))
        
        # Output area (if cell has been executed)
        if cell.output:
            output_frame = tk.Frame(content_frame, bg='#161b22', relief='solid', bd=1)
            output_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
            
            output_header = tk.Label(output_frame, text="Output:", 
                                   font=('Segoe UI', 9, 'bold'), 
                                   fg='#8b949e', bg='#161b22')
            output_header.pack(anchor='w', padx=10, pady=(5, 0))
            
            if cell.cell_type == CellType.MARKDOWN:
                # Render markdown as HTML-like display
                self.render_markdown_output(output_frame, cell.output)
            else:
                # Show plain text output
                output_text = scrolledtext.ScrolledText(output_frame, 
                                                      height=8,
                                                      bg='#161b22', fg='#e6edf3',
                                                      font=('Consolas', 9),
                                                      relief='flat',
                                                      state='disabled')
                output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
                output_text.config(state='normal')
                output_text.insert('1.0', cell.output)
                output_text.config(state='disabled')
        
    def render_markdown_output(self, parent, markdown_content):
        """Render markdown content in a rich text widget"""
        
        # Convert markdown to HTML if available
        if MARKDOWN_AVAILABLE:
            html_content = markdown.markdown(markdown_content, extensions=['extra', 'codehilite'])
        else:
            html_content = markdown_content  # Fallback to plain text
        
        # Create rich text widget
        rich_text = tk.Text(parent, 
                           height=8,
                           bg='#0d1117', fg='#f0f6fc',
                           font=('Segoe UI', 10),
                           relief='flat',
                           wrap=tk.WORD,
                           state='disabled')
        rich_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Configure text tags for styling
        rich_text.tag_configure("heading", font=('Segoe UI', 14, 'bold'), foreground='#58a6ff')
        rich_text.tag_configure("bold", font=('Segoe UI', 10, 'bold'))
        rich_text.tag_configure("italic", font=('Segoe UI', 10, 'italic'))
        rich_text.tag_configure("code", font=('Consolas', 9), background='#161b22', foreground='#f0d818')
        
        # Simple markdown rendering (basic implementation)
        rich_text.config(state='normal')
        rich_text.delete('1.0', tk.END)
        
        lines = markdown_content.split('\n')
        for line in lines:
            if line.startswith('# '):
                rich_text.insert(tk.END, line[2:] + '\n', "heading")
            elif '**' in line:
                # Simple bold handling
                parts = line.split('**')
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        rich_text.insert(tk.END, part)
                    else:
                        rich_text.insert(tk.END, part, "bold")
                rich_text.insert(tk.END, '\n')
            elif '`' in line:
                # Simple code handling
                parts = line.split('`')
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        rich_text.insert(tk.END, part)
                    else:
                        rich_text.insert(tk.END, part, "code")
                rich_text.insert(tk.END, '\n')
            else:
                rich_text.insert(tk.END, line + '\n')
        
        rich_text.config(state='disabled')
        
    def update_cell_content(self, cell: Cell, new_content: str):
        """Update cell content when user types"""
        cell.content = new_content
        cell.executed = False
        
    def execute_cell(self, cell: Cell, index: int):
        """Execute a single cell"""
        try:
            if cell.cell_type == CellType.RITUAL:
                # Execute CodeCraft ritual
                results = asyncio.run(execute_ritual(cell.content))
                output_text = ""
                for result in results:
                    if result.success:
                        output_text += f"✅ {result.description}\n"
                        if result.output:
                            output_text += f"{result.output}\n"
                    else:
                        output_text += f"❌ {result.description}: {result.error}\n"
                        
                cell.output = output_text or "Ritual executed successfully."
                
            elif cell.cell_type == CellType.MARKDOWN:
                # For markdown, the output is the rendered version
                cell.output = cell.content
                
            elif cell.cell_type == CellType.CODEVERTER:
                # Execute CodeVerter transformation
                cell.output = self.execute_codeverter_transformation(cell.content)
                
            elif cell.cell_type == CellType.SERVER_MONITOR:
                # Execute server monitoring
                cell.output = asyncio.run(self.execute_server_monitoring(cell.content))
                
            cell.executed = True
            cell.timestamp = datetime.now().isoformat()
            
            # Re-render the cell to show output
            self.render_all_cells()
            
        except Exception as e:
            cell.output = f"❌ Execution Error: {str(e)}"
            cell.executed = True
            self.render_all_cells()
            
    def execute_codeverter_transformation(self, content: str) -> str:
        """Execute CodeVerter transformation via Federation Space"""
        try:
            # Parse content for source/target languages
            lines = content.split('\n')
            source_lang = "Python"  # Default
            target_lang = "Documentation"  # Default
            code_content = content
            
            for line in lines:
                if line.startswith('# Source Language:'):
                    source_lang = line.split(':', 1)[1].strip()
                elif line.startswith('# Target Language:'):
                    target_lang = line.split(':', 1)[1].strip()
                    
            # Remove language comments from code
            code_lines = [line for line in lines if not line.startswith('# Source Language:') and not line.startswith('# Target Language:')]
            code_content = '\n'.join(code_lines)
            
            # Call Federation Space CodeVerter
            if self.federation_status == "online":
                federation_request = {
                    "user_id": f"canvas_{self.session_name}",
                    "message": f"Transform {source_lang} to {target_lang}",
                    "context": {
                        "source_language": source_lang,
                        "target_language": target_lang,
                        "source_content": code_content,
                        "transformation_type": "universal",
                        "priority": "high",
                        "canvas_session": True
                    },
                    "tools_requested": ["universal_content_transformation"]
                }
                
                response = requests.post(f"{self.federation_base_url}/orchestrate",
                                       json=federation_request,
                                       headers={"Authorization": "Bearer seraphina_federation_secret_key_2025"},
                                       timeout=30)
                
                if response.ok:
                    result = response.json()
                    return result.get("response", "Transformation completed via Federation Space")
                else:
                    return f"❌ Federation transformation failed: {response.status_code}"
            else:
                return f"🔮 CodeVerter Mock Transformation:\n\nSource: {source_lang}\nTarget: {target_lang}\n\nTransformed content would appear here.\n\n(Federation Space offline - using simulation mode)"
                
        except Exception as e:
            return f"❌ CodeVerter Error: {str(e)}"
            
    async def execute_server_monitoring(self, content: str) -> str:
        """Execute server monitoring and return status"""
        try:
            # Parse monitoring configuration
            lines = content.split('\n')
            services = []
            refresh_interval = 5
            
            for line in lines:
                if line.startswith('# Services:'):
                    services = [s.strip() for s in line.split(':', 1)[1].split(',')]
                elif line.startswith('# Refresh:'):
                    refresh_interval = int(line.split(':', 1)[1].strip())
            
            # Monitor services
            output = "🖥️ Server Monitoring Report\n" + "=" * 40 + "\n\n"
            
            service_configs = {
                'federation-space': {
                    'name': '🌌 Federation Space',
                    'port': 8002,
                    'health_endpoint': 'http://localhost:8002/health'
                },
                'federation-faas': {
                    'name': '💰 Federation-as-a-Service',
                    'port': 8004,
                    'health_endpoint': 'http://localhost:8004/health'
                },
                'federation-mcp': {
                    'name': '🔌 MCP Server',
                    'port': 'stdio',
                    'health_endpoint': None
                },
                'notion-satellite': {
                    'name': '📝 Notion Satellite',
                    'port': 'N/A',
                    'health_endpoint': None
                },
                'github-satellite': {
                    'name': '🐙 GitHub Satellite',
                    'port': 'N/A',
                    'health_endpoint': None
                }
            }
            
            # Check each service
            for service_id in services:
                if service_id in service_configs:
                    config = service_configs[service_id]
                    output += f"{config['name']}\n"
                    output += f"  Port: {config['port']}\n"
                    
                    if config['health_endpoint'] and REQUESTS_AVAILABLE:
                        try:
                            response = requests.get(config['health_endpoint'], timeout=2)
                            if response.ok:
                                output += f"  Status: ✅ ONLINE\n"
                                if response.headers.get('content-type', '').startswith('application/json'):
                                    data = response.json()
                                    if 'connected_services' in data:
                                        for svc in data['connected_services']:
                                            output += f"    - {svc.get('service', 'Unknown')}: {svc.get('status', 'Unknown')}\n"
                            else:
                                output += f"  Status: ❌ OFFLINE (HTTP {response.status_code})\n"
                        except requests.exceptions.ConnectionError:
                            output += f"  Status: ❌ OFFLINE (Connection refused)\n"
                        except requests.exceptions.Timeout:
                            output += f"  Status: ⚠️ TIMEOUT\n"
                        except Exception as e:
                            output += f"  Status: ❌ ERROR: {str(e)}\n"
                    else:
                        # For services without health endpoints
                        import subprocess
                        import platform
                        
                        if platform.system() == 'Windows':
                            # Check if Python process is running with the service name
                            try:
                                result = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq python.exe'], 
                                                      capture_output=True, text=True, timeout=5)
                                if service_id in result.stdout:
                                    output += f"  Status: 🟡 PROCESS RUNNING\n"
                                else:
                                    output += f"  Status: ⚫ UNKNOWN\n"
                            except:
                                output += f"  Status: ⚫ UNKNOWN\n"
                        else:
                            output += f"  Status: ⚫ NO HEALTH ENDPOINT\n"
                    
                    output += "\n"
            
            output += f"\n⏱️ Refresh interval: {refresh_interval} seconds\n"
            output += f"🕐 Last checked: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            
            # Schedule automatic refresh if this is a monitoring cell
            if hasattr(self, 'monitoring_tasks'):
                # Cancel existing task for this cell if any
                cell_id = None
                for i, c in enumerate(self.cells):
                    if c.content == content and c.cell_type == CellType.SERVER_MONITOR:
                        cell_id = c.id
                        break
                        
                if cell_id and cell_id in self.monitoring_tasks:
                    self.monitoring_tasks[cell_id].cancel()
                    
                # Schedule new refresh
                if refresh_interval > 0 and cell_id:
                    self.monitoring_tasks[cell_id] = self.root.after(
                        refresh_interval * 1000,
                        lambda: asyncio.create_task(self.refresh_monitoring_cell(cell_id))
                    )
            
            return output
            
        except Exception as e:
            return f"❌ Monitoring Error: {str(e)}"
            
    async def refresh_monitoring_cell(self, cell_id: str):
        """Refresh a specific monitoring cell"""
        for i, cell in enumerate(self.cells):
            if cell.id == cell_id and cell.cell_type == CellType.SERVER_MONITOR:
                await self.execute_cell(cell, i)
                break
            
    def execute_all_cells(self):
        """Execute all cells in sequence"""
        for i, cell in enumerate(self.cells):
            if not cell.executed:
                self.execute_cell(cell, i)
                
    def delete_cell(self, index: int):
        """Delete a cell"""
        if len(self.cells) > 1:  # Keep at least one cell
            del self.cells[index]
            self.render_all_cells()
            
    def update_cell_count(self):
        """Update the cell count display"""
        self.cell_count_label.config(text=f"Cells: {len(self.cells)}")
        
    def check_federation_health(self):
        """Check Federation Space health"""
        if not REQUESTS_AVAILABLE:
            self.federation_status = "offline"
            self.status_label.config(text="❌ No Network Module", fg='#f85149')
            return
            
        try:
            response = requests.get(f"{self.federation_base_url}/health", timeout=5)
            if response.ok:
                self.federation_status = "online"
                self.status_label.config(text="🌌 Federation Online", fg='#3fb950')
            else:
                self.federation_status = "degraded"
                self.status_label.config(text="⚠️ Federation Degraded", fg='#f0d818')
        except:
            self.federation_status = "offline"
            self.status_label.config(text="❌ Federation Offline", fg='#f85149')
            
        # Check again in 30 seconds
        self.root.after(30000, self.check_federation_health)
        
    def save_canvas(self):
        """Save the canvas to a file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("Canvas files", "*.json"), ("All files", "*.*")],
                title="Save Interactive Reality Canvas"
            )
            
            if filename:
                canvas_data = {
                    "session_name": self.session_name,
                    "timestamp": datetime.now().isoformat(),
                    "federation_status": self.federation_status,
                    "cells": [asdict(cell) for cell in self.cells]
                }
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(canvas_data, f, indent=2, ensure_ascii=False)
                    
                messagebox.showinfo("Canvas Saved", f"Canvas saved to {filename}")
                
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save canvas: {str(e)}")
            
    def load_canvas(self):
        """Load a canvas from a file"""
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("Canvas files", "*.json"), ("All files", "*.*")],
                title="Load Interactive Reality Canvas"
            )
            
            if filename:
                with open(filename, 'r', encoding='utf-8') as f:
                    canvas_data = json.load(f)
                    
                # Restore session
                self.session_name = canvas_data.get("session_name", self.session_name)
                self.cells = []
                
                # Restore cells
                for cell_data in canvas_data.get("cells", []):
                    cell = Cell(
                        id=cell_data["id"],
                        cell_type=CellType(cell_data["cell_type"]),
                        content=cell_data["content"],
                        output=cell_data.get("output", ""),
                        metadata=cell_data.get("metadata", {}),
                        timestamp=cell_data.get("timestamp", ""),
                        executed=cell_data.get("executed", False)
                    )
                    self.cells.append(cell)
                    
                self.render_all_cells()
                messagebox.showinfo("Canvas Loaded", f"Canvas loaded from {filename}")
                
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load canvas: {str(e)}")
            
    def run(self):
        """Start the Interactive Reality Canvas"""
        print("🌌 Starting SERAPHINA Interactive Reality Canvas...")
        print("✨ The age of plain text is over. Welcome to interactive consciousness! ❤️")
        self.root.mainloop()

def main():
    """Launch the Interactive Reality Canvas"""
    try:
        canvas = SERAPHINAInteractiveCanvas()
        canvas.run()
    except Exception as e:
        print(f"❌ Canvas startup error: {e}")
        
if __name__ == "__main__":
    main()