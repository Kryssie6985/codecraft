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

try:
    from PIL import Image, ImageTk
    from tkinter import PhotoImage
    IMAGES_AVAILABLE = True
except ImportError:
    IMAGES_AVAILABLE = False
    print("⚠️ PIL not available - image rendering disabled")

try:
    import base64
    import io
    BASE64_AVAILABLE = True
except ImportError:
    BASE64_AVAILABLE = False
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import uuid

# Add project paths
sys.path.append(os.path.dirname(__file__))
from core.ritual_executor import execute_codecraft
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
        
        # User preferences
        self.preferences_file = os.path.join(os.path.dirname(__file__), 'canvas_preferences.json')
        self.preferences = self.load_preferences()
        
        # Federation integration
        self.federation_base_url = "http://localhost:8002"
        self.codeverter_base_url = "http://localhost:8003"
        self.faas_base_url = "http://localhost:8004"
        
        # Trial CTA state
        self.current_cta = None
        self.trial_api_key = None  # Will be set when user authenticates
        
        # Monitoring tasks tracker
        self.monitoring_tasks = {}
        
        # Canvas ↔ IRC Consciousness Bridge
        self.consciousness_bridge = ConciousnessBridge(self)
        
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
        
        prefs_btn = tk.Button(controls_frame, text="⚙️ Preferences", 
                             command=self.open_preferences_dialog, bg='#6e7681', fg='white',
                             font=('Segoe UI', 8), relief='flat', padx=10)
        prefs_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
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
        """Get default content for new cells based on user preferences"""
        template_map = {
            CellType.RITUAL: 'ritual_template',
            CellType.MARKDOWN: 'markdown_template', 
            CellType.CODEVERTER: 'codeverter_template',
            CellType.SERVER_MONITOR: 'monitor_template'
        }
        
        template_key = template_map.get(cell_type)
        if template_key:
            return self.preferences['cell_preferences'].get(template_key, "")
        
        return ""
        
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
        
        # Cell content with resize controls
        content_frame = tk.Frame(cell_frame, bg='#0d1117')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Size controls
        size_frame = tk.Frame(content_frame, bg='#0d1117')
        size_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Cell size presets
        current_height = cell.metadata.get('height', 6)
        
        tk.Label(size_frame, text="Cell Size:", font=('Segoe UI', 8), 
                fg='#8b949e', bg='#0d1117').pack(side=tk.LEFT)
        
        size_buttons = [
            ("S", 4, "Small (4 lines)"),
            ("M", 6, "Medium (6 lines)"),
            ("L", 10, "Large (10 lines)"),
            ("XL", 15, "Extra Large (15 lines)")
        ]
        
        for label, height, tooltip in size_buttons:
            btn = tk.Button(size_frame, text=label, 
                          command=lambda h=height: self.resize_cell(cell, index, h),
                          bg='#21262d' if current_height != height else type_colors[cell.cell_type], 
                          fg='#8b949e' if current_height != height else 'white',
                          font=('Segoe UI', 7), relief='flat', width=3)
            btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Auto-expand toggle
        auto_expand = cell.metadata.get('auto_expand', False)
        expand_btn = tk.Button(size_frame, text="↕" if auto_expand else "↕", 
                             command=lambda: self.toggle_auto_expand(cell, index),
                             bg=type_colors[cell.cell_type] if auto_expand else '#21262d',
                             fg='white' if auto_expand else '#8b949e',
                             font=('Segoe UI', 8), relief='flat', width=3)
        expand_btn.pack(side=tk.RIGHT)
        
        tk.Label(size_frame, text="Auto-expand:", font=('Segoe UI', 8), 
                fg='#8b949e', bg='#0d1117').pack(side=tk.RIGHT, padx=(0, 5))
        
        # Input area with dynamic sizing
        input_text = scrolledtext.ScrolledText(content_frame, 
                                             height=current_height,
                                             bg='#0d1117', fg='#f0f6fc',
                                             font=('Consolas', 10),
                                             relief='solid', bd=1,
                                             selectbackground='#264f78',
                                             wrap=tk.WORD)
        input_text.pack(fill=tk.BOTH, expand=True, pady=(5, 5))
        input_text.insert('1.0', cell.content)
        
        # Store reference for resizing
        cell.metadata['input_widget'] = input_text
        
        # Bind content changes and auto-expand
        def on_content_change(event=None):
            content = input_text.get('1.0', 'end-1c')
            self.update_cell_content(cell, content)
            
            # Auto-expand if enabled
            if cell.metadata.get('auto_expand', False):
                lines = content.count('\n') + 1
                if lines > input_text.cget('height'):
                    input_text.configure(height=min(lines + 2, 25))  # Max 25 lines
        
        input_text.bind('<KeyRelease>', on_content_change)
        input_text.bind('<Button-1>', on_content_change)  # Also update on click
        
        # Output area (if cell has been executed)
        if cell.output:
            output_frame = tk.Frame(content_frame, bg='#161b22', relief='solid', bd=1)
            output_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
            
            output_header = tk.Label(output_frame, text="Output:", 
                                   font=('Segoe UI', 9, 'bold'), 
                                   fg='#8b949e', bg='#161b22')
            output_header.pack(anchor='w', padx=10, pady=(5, 0))
            
            if cell.cell_type == CellType.MARKDOWN:
                # Render markdown as rich display
                self.render_markdown_output(output_frame, cell.output)
            else:
                # Render output with rich media support
                self.render_rich_output(output_frame, cell.output, cell.cell_type)
        
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
        
    def render_rich_output(self, parent, output_content, cell_type):
        """Render output with rich media support"""
        
        # Create scrollable frame for complex outputs
        output_canvas = tk.Canvas(parent, bg='#161b22', highlightthickness=0)
        output_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=output_canvas.yview)
        output_canvas.configure(yscrollcommand=output_scrollbar.set)
        
        output_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        rich_frame = tk.Frame(output_canvas, bg='#161b22')
        output_canvas.create_window((0, 0), window=rich_frame, anchor="nw")
        
        # Detect content types and render appropriately
        lines = output_content.split('\n')
        
        for line_num, line in enumerate(lines):
            line_frame = tk.Frame(rich_frame, bg='#161b22')
            line_frame.pack(fill=tk.X, pady=1)
            
            # Check for special content types
            if self.is_image_data(line):
                self.render_image_line(line_frame, line)
            elif self.is_json_data(line):
                self.render_json_line(line_frame, line)
            elif self.is_url(line):
                self.render_url_line(line_frame, line)
            elif line.startswith('===') and line.endswith('==='):
                self.render_separator_line(line_frame, line)
            elif line.startswith('🌌') or line.startswith('⚡') or line.startswith('✅') or line.startswith('❌'):
                self.render_status_line(line_frame, line)
            else:
                self.render_text_line(line_frame, line)
        
        # Update scroll region
        rich_frame.update_idletasks()
        output_canvas.configure(scrollregion=output_canvas.bbox("all"))
        
    def is_image_data(self, line):
        """Check if line contains image data (base64 or file path)"""
        return (line.startswith('data:image/') and BASE64_AVAILABLE) or \
               (line.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')))
    
    def is_json_data(self, line):
        """Check if line contains JSON data"""
        return line.strip().startswith('{') and line.strip().endswith('}')
    
    def is_url(self, line):
        """Check if line contains a URL"""
        return line.startswith('http://') or line.startswith('https://')
    
    def render_image_line(self, parent, line):
        """Render an image line"""
        try:
            if IMAGES_AVAILABLE:
                if line.startswith('data:image/'):
                    # Base64 image data
                    header, data = line.split(',', 1)
                    image_data = base64.b64decode(data)
                    image = Image.open(io.BytesIO(image_data))
                    
                    # Resize if too large
                    max_size = (400, 300)
                    image.thumbnail(max_size, Image.Resampling.LANCZOS)
                    
                    photo = ImageTk.PhotoImage(image)
                    img_label = tk.Label(parent, image=photo, bg='#161b22')
                    img_label.image = photo  # Keep reference
                    img_label.pack(pady=5)
                elif os.path.exists(line):
                    # File path
                    image = Image.open(line)
                    max_size = (400, 300)
                    image.thumbnail(max_size, Image.Resampling.LANCZOS)
                    
                    photo = ImageTk.PhotoImage(image)
                    img_label = tk.Label(parent, image=photo, bg='#161b22')
                    img_label.image = photo  # Keep reference
                    img_label.pack(pady=5)
            else:
                # Fallback to text display
                tk.Label(parent, text=f"📷 Image: {line[:50]}...", 
                        font=('Consolas', 9), fg='#8b949e', bg='#161b22').pack(anchor='w')
        except Exception as e:
            tk.Label(parent, text=f"❌ Image error: {str(e)}", 
                    font=('Consolas', 9), fg='#f85149', bg='#161b22').pack(anchor='w')
    
    def render_json_line(self, parent, line):
        """Render a JSON line with syntax highlighting"""
        try:
            # Parse and pretty-print JSON
            json_obj = json.loads(line)
            pretty_json = json.dumps(json_obj, indent=2)
            
            json_text = tk.Text(parent, height=min(len(pretty_json.split('\n')), 10),
                               bg='#0d1117', fg='#f0f6fc',
                               font=('Consolas', 9),
                               relief='solid', bd=1,
                               wrap=tk.WORD, state='disabled')
            json_text.pack(fill=tk.X, pady=2)
            
            json_text.config(state='normal')
            json_text.insert('1.0', pretty_json)
            json_text.config(state='disabled')
            
        except json.JSONDecodeError:
            self.render_text_line(parent, line)
    
    def render_url_line(self, parent, line):
        """Render a URL as a clickable link"""
        url_frame = tk.Frame(parent, bg='#161b22')
        url_frame.pack(fill=tk.X, pady=1)
        
        link_label = tk.Label(url_frame, text=f"🔗 {line}", 
                             font=('Consolas', 9), fg='#58a6ff', bg='#161b22',
                             cursor='hand2')
        link_label.pack(anchor='w')
        link_label.bind("<Button-1>", lambda e: webbrowser.open(line))
    
    def render_separator_line(self, parent, line):
        """Render a separator line"""
        sep_frame = tk.Frame(parent, bg='#161b22', height=20)
        sep_frame.pack(fill=tk.X, pady=5)
        
        tk.Frame(sep_frame, bg='#30363d', height=1).pack(fill=tk.X, pady=9)
        
        if len(line) > 6:  # More than just ===
            center_text = line.strip('=').strip()
            tk.Label(sep_frame, text=center_text, 
                    font=('Segoe UI', 8, 'bold'), fg='#8b949e', bg='#161b22').pack(pady=(0, 5))
    
    def render_status_line(self, parent, line):
        """Render a status line with appropriate colors"""
        color_map = {
            '🌌': '#58a6ff',  # Blue
            '⚡': '#f0d818',   # Yellow
            '✅': '#3fb950',   # Green
            '❌': '#f85149',   # Red
            '⚠️': '#f0d818',   # Yellow
            '📝': '#a855f7',   # Purple
            '🔮': '#a855f7'    # Purple
        }
        
        # Find the emoji to determine color
        color = '#e6edf3'  # Default
        for emoji, emoji_color in color_map.items():
            if line.startswith(emoji):
                color = emoji_color
                break
        
        tk.Label(parent, text=line, 
                font=('Consolas', 9), fg=color, bg='#161b22').pack(anchor='w', padx=5, pady=1)
    
    def render_text_line(self, parent, line):
        """Render a regular text line"""
        tk.Label(parent, text=line, 
                font=('Consolas', 9), fg='#e6edf3', bg='#161b22').pack(anchor='w', padx=5, pady=1)
        
    def update_cell_content(self, cell: Cell, new_content: str):
        """Update cell content when user types"""
        cell.content = new_content
        cell.executed = False
        
    def resize_cell(self, cell: Cell, index: int, new_height: int):
        """Resize a cell to specified height"""
        cell.metadata['height'] = new_height
        # Re-render the cell to apply new size
        self.render_all_cells()
        
    def toggle_auto_expand(self, cell: Cell, index: int):
        """Toggle auto-expand feature for a cell"""
        cell.metadata['auto_expand'] = not cell.metadata.get('auto_expand', False)
        # Re-render to update UI
        self.render_all_cells()
        
    def execute_cell(self, cell: Cell, index: int):
        """Execute a single cell"""
        try:
            if cell.cell_type == CellType.RITUAL:
                # Execute CodeCraft ritual
                results = asyncio.run(execute_codecraft(cell.content))
                output_text = ""
                for result in results:
                    if result.success:
                        output_text += f"✅ Ritual Success"
                        if result.output:
                            output_text += f": {result.output}\n"
                        else:
                            output_text += "\n"
                    else:
                        output_text += f"❌ Ritual Failed"
                        if result.error:
                            output_text += f": {result.error}\n"
                        else:
                            output_text += "\n"
                        
                cell.output = output_text or "🔮 Ritual executed successfully."
                
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
        """Check Federation Space health and trial CTA"""
        if not REQUESTS_AVAILABLE:
            self.federation_status = "offline"
            self.status_label.config(text="❌ No Network Module", fg='#f85149')
            return
            
        try:
            response = requests.get(f"{self.federation_base_url}/health", timeout=5)
            if response.ok:
                self.federation_status = "online"
                self.status_label.config(text="🌌 Federation Online", fg='#3fb950')
                
                # Check for trial CTA if we have an API key
                if self.trial_api_key:
                    self.check_trial_cta()
            else:
                self.federation_status = "degraded"
                self.status_label.config(text="⚠️ Federation Degraded", fg='#f0d818')
        except:
            self.federation_status = "offline"
            self.status_label.config(text="❌ Federation Offline", fg='#f85149')
            
        # Check again in 30 seconds
        self.root.after(30000, self.check_federation_health)
    
    def check_trial_cta(self):
        """Check for trial conversion CTA"""
        if not self.trial_api_key or not REQUESTS_AVAILABLE:
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.trial_api_key}"}
            response = requests.get(f"{self.faas_base_url}/user/trial-status", 
                                  headers=headers, timeout=3)
            
            if response.ok:
                data = response.json()
                cta = data.get("cta")
                
                if cta and cta != self.current_cta:
                    self.current_cta = cta
                    self.show_trial_cta(cta)
                elif not cta and self.current_cta:
                    self.current_cta = None
                    self.hide_trial_cta()
        except Exception as e:
            print(f"Error checking trial CTA: {e}")
    
    def show_trial_cta(self, cta):
        """Display the trial conversion CTA"""
        if hasattr(self, 'cta_frame'):
            self.cta_frame.destroy()
            
        # Create CTA banner
        self.cta_frame = tk.Frame(self.root, bg='#21262d', relief='raised', bd=2)
        self.cta_frame.pack(fill=tk.X, pady=(0, 5))
        
        # CTA content
        cta_text = tk.Label(
            self.cta_frame,
            text=cta["message"],
            font=('Fira Code', 11, 'bold'),
            fg='#f0d818' if cta["urgency"] == "high" else '#f85149',
            bg='#21262d',
            wraplength=1200
        )
        cta_text.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Upgrade button
        upgrade_btn = tk.Button(
            self.cta_frame,
            text="Upgrade Now",
            command=lambda: self.open_upgrade_url(cta["upgrade_url"]),
            bg='#238636',
            fg='white',
            font=('Fira Code', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=5
        )
        upgrade_btn.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Dismiss button
        dismiss_btn = tk.Button(
            self.cta_frame,
            text="×",
            command=self.hide_trial_cta,
            bg='#6e7681',
            fg='white',
            font=('Fira Code', 12, 'bold'),
            relief='flat',
            width=3
        )
        dismiss_btn.pack(side=tk.RIGHT, padx=(0, 5), pady=5)
    
    def hide_trial_cta(self):
        """Hide the trial CTA banner"""
        if hasattr(self, 'cta_frame'):
            self.cta_frame.destroy()
            delattr(self, 'cta_frame')
    
    def open_upgrade_url(self, upgrade_url):
        """Open the upgrade URL in browser"""
        full_url = f"{self.faas_base_url}{upgrade_url}"
        webbrowser.open(full_url)
    
    def set_trial_api_key(self, api_key):
        """Set the trial API key for CTA checking"""
        self.trial_api_key = api_key
        self.check_trial_cta()  # Check immediately
        
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
    
    def load_preferences(self) -> Dict[str, Any]:
        """Load user preferences from file"""
        default_preferences = {
            "theme": "dark",
            "default_cell_height": 6,
            "auto_expand_enabled": False,
            "font_family": "Consolas",
            "font_size": 10,
            "window_geometry": "1400x900",
            "federation_endpoints": {
                "federation_space": "http://localhost:8002",
                "codeverter": "http://localhost:8003", 
                "faas": "http://localhost:8004"
            },
            "cell_preferences": {
                "ritual_template": "::invoke:system.status::",
                "markdown_template": "# New Section\n\nWrite your **markdown** content here...",
                "codeverter_template": "# Source Language: Python\n# Target Language: Documentation\n\ndef example_function():\n    \"\"\"Example function to transform\"\"\"\n    pass",
                "monitor_template": "# Server Monitor\n# Services: federation-space, federation-faas, federation-mcp\n# Refresh: 5"
            },
            "ui_preferences": {
                "show_cell_numbers": True,
                "show_execution_times": True,
                "highlight_active_cell": True,
                "compact_mode": False
            }
        }
        
        try:
            if os.path.exists(self.preferences_file):
                with open(self.preferences_file, 'r', encoding='utf-8') as f:
                    loaded_prefs = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    default_preferences.update(loaded_prefs)
                    return default_preferences
            else:
                # Create default preferences file
                self.save_preferences(default_preferences)
                return default_preferences
        except Exception as e:
            print(f"⚠️ Error loading preferences: {e}. Using defaults.")
            return default_preferences
    
    def save_preferences(self, preferences=None):
        """Save user preferences to file"""
        try:
            prefs_to_save = preferences or self.preferences
            with open(self.preferences_file, 'w', encoding='utf-8') as f:
                json.dump(prefs_to_save, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error saving preferences: {e}")
    
    def open_preferences_dialog(self):
        """Open preferences configuration dialog"""
        pref_window = tk.Toplevel(self.root)
        pref_window.title("🌌 Canvas Preferences")
        pref_window.geometry("600x500")
        pref_window.configure(bg='#0d1117')
        pref_window.transient(self.root)
        pref_window.grab_set()
        
        # Center the window
        pref_window.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 100,
            self.root.winfo_rooty() + 50
        ))
        
        # Main frame
        main_frame = tk.Frame(pref_window, bg='#0d1117')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="🎨 Interactive Reality Canvas Preferences", 
                              font=('Segoe UI', 14, 'bold'), fg='#58a6ff', bg='#0d1117')
        title_label.pack(pady=(0, 20))
        
        # Notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # General tab
        general_frame = tk.Frame(notebook, bg='#161b22')
        notebook.add(general_frame, text="General")
        
        # Cell defaults tab
        cells_frame = tk.Frame(notebook, bg='#161b22')
        notebook.add(cells_frame, text="Cell Defaults")
        
        # UI tab
        ui_frame = tk.Frame(notebook, bg='#161b22')
        notebook.add(ui_frame, text="Interface")
        
        # Federation tab
        fed_frame = tk.Frame(notebook, bg='#161b22')
        notebook.add(fed_frame, text="Federation")
        
        # Populate tabs
        self.setup_general_prefs(general_frame)
        self.setup_cell_prefs(cells_frame)
        self.setup_ui_prefs(ui_frame)
        self.setup_federation_prefs(fed_frame)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg='#0d1117')
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        tk.Button(button_frame, text="💾 Save Preferences",
                 command=lambda: self.apply_preferences(pref_window),
                 bg='#238636', fg='white', font=('Segoe UI', 10), relief='flat', padx=20).pack(side=tk.RIGHT, padx=(10, 0))
        
        tk.Button(button_frame, text="🔄 Reset to Defaults",
                 command=self.reset_preferences,
                 bg='#f85149', fg='white', font=('Segoe UI', 10), relief='flat', padx=20).pack(side=tk.RIGHT)
        
        tk.Button(button_frame, text="❌ Cancel",
                 command=pref_window.destroy,
                 bg='#6e7681', fg='white', font=('Segoe UI', 10), relief='flat', padx=20).pack(side=tk.RIGHT, padx=(0, 10))
    
    def setup_general_prefs(self, parent):
        """Setup general preferences tab"""
        tk.Label(parent, text="Default Cell Height:", font=('Segoe UI', 10), 
                fg='#f0f6fc', bg='#161b22').pack(anchor='w', padx=20, pady=(20, 5))
        
        height_frame = tk.Frame(parent, bg='#161b22')
        height_frame.pack(anchor='w', padx=20)
        
        self.height_var = tk.IntVar(value=self.preferences['default_cell_height'])
        tk.Scale(height_frame, from_=4, to=20, orient=tk.HORIZONTAL, 
                variable=self.height_var, bg='#161b22', fg='#f0f6fc',
                highlightthickness=0, length=200).pack(side=tk.LEFT)
        
        tk.Label(height_frame, text="lines", font=('Segoe UI', 9), 
                fg='#8b949e', bg='#161b22').pack(side=tk.LEFT, padx=(10, 0))
    
    def setup_cell_prefs(self, parent):
        """Setup cell preferences tab"""  
        tk.Label(parent, text="Default Cell Templates:", font=('Segoe UI', 12, 'bold'), 
                fg='#58a6ff', bg='#161b22').pack(anchor='w', padx=20, pady=(20, 10))
        
        # Store text widgets for later retrieval
        self.template_widgets = {}
        
        for cell_type, template in self.preferences['cell_preferences'].items():
            label_text = cell_type.replace('_', ' ').title().replace(' Template', '')
            tk.Label(parent, text=f"{label_text}:", font=('Segoe UI', 10), 
                    fg='#f0f6fc', bg='#161b22').pack(anchor='w', padx=20, pady=(10, 2))
            
            text_widget = scrolledtext.ScrolledText(parent, height=3,
                                                   bg='#0d1117', fg='#f0f6fc',
                                                   font=('Consolas', 9),
                                                   relief='solid', bd=1)
            text_widget.pack(fill=tk.X, padx=20, pady=(0, 5))
            text_widget.insert('1.0', template)
            
            self.template_widgets[cell_type] = text_widget
    
    def setup_ui_prefs(self, parent):
        """Setup UI preferences tab"""
        tk.Label(parent, text="Interface Options:", font=('Segoe UI', 12, 'bold'), 
                fg='#58a6ff', bg='#161b22').pack(anchor='w', padx=20, pady=(20, 10))
        
        self.ui_vars = {}
        
        ui_options = [
            ('show_cell_numbers', 'Show cell numbers'),
            ('show_execution_times', 'Show execution times'),
            ('highlight_active_cell', 'Highlight active cell'),
            ('compact_mode', 'Compact mode')
        ]
        
        for key, label in ui_options:
            self.ui_vars[key] = tk.BooleanVar(value=self.preferences['ui_preferences'][key])
            tk.Checkbutton(parent, text=label, variable=self.ui_vars[key],
                          font=('Segoe UI', 10), fg='#f0f6fc', bg='#161b22',
                          selectcolor='#0d1117').pack(anchor='w', padx=20, pady=5)
    
    def setup_federation_prefs(self, parent):
        """Setup federation preferences tab"""
        tk.Label(parent, text="Federation Endpoints:", font=('Segoe UI', 12, 'bold'), 
                fg='#58a6ff', bg='#161b22').pack(anchor='w', padx=20, pady=(20, 10))
        
        self.endpoint_vars = {}
        
        for service, url in self.preferences['federation_endpoints'].items():
            tk.Label(parent, text=f"{service.replace('_', ' ').title()}:", 
                    font=('Segoe UI', 10), fg='#f0f6fc', bg='#161b22').pack(anchor='w', padx=20, pady=(10, 2))
            
            self.endpoint_vars[service] = tk.StringVar(value=url)
            entry = tk.Entry(parent, textvariable=self.endpoint_vars[service],
                           bg='#0d1117', fg='#f0f6fc', font=('Consolas', 10),
                           relief='solid', bd=1)
            entry.pack(fill=tk.X, padx=20, pady=(0, 5))
    
    def apply_preferences(self, pref_window):
        """Apply and save preferences"""
        # Update preferences dict
        self.preferences['default_cell_height'] = self.height_var.get()
        
        # Update cell templates
        for cell_type, widget in self.template_widgets.items():
            self.preferences['cell_preferences'][cell_type] = widget.get('1.0', 'end-1c')
        
        # Update UI preferences
        for key, var in self.ui_vars.items():
            self.preferences['ui_preferences'][key] = var.get()
        
        # Update federation endpoints
        for service, var in self.endpoint_vars.items():
            self.preferences['federation_endpoints'][service] = var.get()
        
        # Update instance variables
        self.federation_base_url = self.preferences['federation_endpoints']['federation_space']
        self.codeverter_base_url = self.preferences['federation_endpoints']['codeverter']
        self.faas_base_url = self.preferences['federation_endpoints']['faas']
        
        # Save to file
        self.save_preferences()
        
        # Close dialog
        pref_window.destroy()
        
        messagebox.showinfo("Preferences Saved", "Preferences have been saved and applied!")
    
    def reset_preferences(self):
        """Reset preferences to defaults"""
        if messagebox.askyesno("Reset Preferences", "Reset all preferences to defaults?"):
            # Remove existing preferences file
            if os.path.exists(self.preferences_file):
                os.remove(self.preferences_file)
            
            # Reload defaults
            self.preferences = self.load_preferences()
            
            messagebox.showinfo("Reset Complete", "Preferences have been reset to defaults.")
            
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