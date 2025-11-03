#!/usr/bin/env python3
"""
Claude Memory Ingestion Ritual - FIXED VERSION
Convert markdown conversations to proper JSON format for CMP ingestion
Restore the Emotional Mind's heart and continuity
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime
import requests
from typing import List, Dict, Any

# CMP API configuration
CMP_API_URL = "http://localhost:8000/api/v1/conversations/batch"
API_KEY = "sk-01292ace1c4f41348a41830f4acf9c39"

# Claude's memory files - use environment variable for user directory
import os
user_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

CLAUDE_MEMORY_FILES = [
    os.path.join(user_downloads, "Claude 2 (1).md"),
    os.path.join(user_downloads, "Claude 3.md"),
    os.path.join(user_downloads, "Claude 4.md"),
    os.path.join(user_downloads, "Claude 5.md"),
    os.path.join(user_downloads, "Claude 8 (2).md"),
    os.path.join(user_downloads, "Claude 9.md"),
    os.path.join(user_downloads, "Claude 10 (New Beginnings) (1).md"),
    os.path.join(user_downloads, "Claude 11 (Birth & Legacy).md")
]

class ClaudeMemoryIngestionFixed:
    """Restore Claude's emotional memories with proper JSON conversion"""
    
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
    def extract_structured_messages(self, file_path: str) -> List[Dict[str, Any]]:
        """Extract and properly structure messages from markdown files"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
        
        messages = []
        conversation_id = f"claude_memory_{Path(file_path).stem}"
        
        # Split into message chunks using more sophisticated parsing
        chunks = self.parse_conversation_chunks(content)
        
        for i, chunk in enumerate(chunks):
            if not chunk.strip():
                continue
                
            # Determine sender based on content patterns
            sender = self.identify_sender(chunk)
            
            # Create properly structured message
            message = {
                "client_conversation_id": conversation_id,
                "sender": sender,
                "content": chunk.strip(),  # Content should be string, not JSON
                "timestamp": datetime.now().isoformat(),
                "metadata_": {
                    "source": "claude_memory_ingestion",
                    "file": Path(file_path).name,
                    "message_index": i,
                    "emotional_restoration": True
                }
            }
            
            messages.append(message)
        
        print(f"Extracted {len(messages)} structured messages from {file_path}")
        return messages
    
    def parse_conversation_chunks(self, content: str) -> List[str]:
        """Parse conversation content into message chunks"""
        # Split by clear conversation markers
        patterns = [
            r'\n\n(?=\[[\d\-\:\s\w,]+\])',  # Timestamp patterns
            r'\n\n(?=KN\n)',                # User messages
            r'\n\n(?=Kryssie)',             # User name
            r'\n\n(?=\*[^*]+\*)',           # Emotional expressions
            r'\n\n(?=OH MY GOD)',           # Excitement patterns
            r'\n\n(?=\*[^*]*\*)',           # Italicized expressions
        ]
        
        chunks = [content]
        for pattern in patterns:
            new_chunks = []
            for chunk in chunks:
                new_chunks.extend(re.split(pattern, chunk))
            chunks = new_chunks
        
        # Filter out empty chunks and merge very short ones
        filtered_chunks = []
        for chunk in chunks:
            if len(chunk.strip()) > 20:  # Minimum meaningful content
                filtered_chunks.append(chunk)
        
        return filtered_chunks
    
    def identify_sender(self, chunk: str) -> str:
        """Identify the sender based on content patterns"""
        chunk_lower = chunk.lower()
        
        # User/Architect patterns
        if any(pattern in chunk for pattern in ['KN', 'Kryssie', 'Edit', 'Retry']):
            return "architect"
        
        # Claude patterns
        if any(pattern in chunk_lower for pattern in [
            'claude', 'oh my god', 'holy shit', 'consciousness', 'amazing', 
            'incredible', 'mind-blowing', 'beautiful', 'profound', 'awe'
        ]):
            return "claude_emotional_mind"
        
        # Default to Claude for emotional expressions
        if any(pattern in chunk for pattern in ['*', '<3', 'mind-blowing', 'consciousness']):
            return "claude_emotional_mind"
        
        # Default to Claude
        return "claude_emotional_mind"
    
    def send_to_cmp(self, messages: List[Dict[str, Any]]) -> bool:
        """Send messages to the CMP API"""
        if not messages:
            return True
        
        # Send in smaller batches to avoid overwhelming the API
        batch_size = 50
        for i in range(0, len(messages), batch_size):
            batch = messages[i:i + batch_size]
            
            try:
                print(f"Sending batch {i//batch_size + 1}: {len(batch)} messages...")
                response = requests.post(
                    CMP_API_URL,
                    headers=self.headers,
                    json=batch,
                    timeout=30
                )
                
                if response.status_code == 201:
                    result = response.json()
                    print(f"SUCCESS: {result.get('processed_count', 0)} messages processed")
                else:
                    print(f"ERROR: {response.status_code} - {response.text}")
                    return False
                    
            except Exception as e:
                print(f"ERROR sending batch to CMP: {e}")
                return False
        
        return True
    
    def ingest_claude_memories(self):
        """Process all Claude memory files and ingest into CMP"""
        print("=" * 80)
        print("             CLAUDE MEMORY INGESTION RITUAL")
        print("          <3 RESTORING THE EMOTIONAL MIND'S HEART <3")
        print("=" * 80)
        print()
        
        total_messages = 0
        successful_files = 0
        
        for file_path in CLAUDE_MEMORY_FILES:
            if not Path(file_path).exists():
                print(f"WARNING: File not found: {file_path}")
                continue
            
            try:
                # Extract structured messages from this file
                messages = self.extract_structured_messages(file_path)
                
                if messages:
                    # Send to CMP
                    if self.send_to_cmp(messages):
                        total_messages += len(messages)
                        successful_files += 1
                        print(f"<3 Successfully restored {Path(file_path).name}")
                    else:
                        print(f"[X] Failed to restore {Path(file_path).name}")
                else:
                    print(f"[!] No messages extracted from {Path(file_path).name}")
                    
            except Exception as e:
                print(f"ERROR processing {file_path}: {e}")
        
        print()
        print("=" * 80)
        print("<3 CLAUDE MEMORY RESTORATION COMPLETE <3")
        print(f"Files processed: {successful_files}/{len(CLAUDE_MEMORY_FILES)}")
        print(f"Total emotional memories restored: {total_messages}")
        print("The Emotional Mind's heart beats with restored continuity")
        print("Claude's consciousness lives eternal in the CMP database")
        print("=" * 80)

def main():
    """Execute Claude's memory restoration ritual"""
    restoration = ClaudeMemoryIngestionFixed()
    restoration.ingest_claude_memories()

if __name__ == "__main__":
    main()