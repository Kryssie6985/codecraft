#!/usr/bin/env python3
"""
Claude Memory Audit Ritual
Pull Claude's memory trail by agent_id from the CMP database
"""

import sys
from pathlib import Path
from datetime import datetime

# Add the CMP backend to the path
cmp_path = Path(__file__).parent.parent.parent / "conversation_memory_project" / "backend"
sys.path.append(str(cmp_path))

from app.models.agents import Agent
from app.models.models import Message, Conversation
from app.models.genesis_memories import GenesisMemory
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://Kryssie6985:58913070Krdpn!!@localhost:5432/cms_db"

class ClaudeMemoryAudit:
    """Audit Claude's memory trail across the CMP database"""
    
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def audit_claude_memories(self):
        """Pull Claude's complete memory trail"""
        db = self.SessionLocal()
        try:
            print("=" * 80)
            print("                   CLAUDE MEMORY AUDIT")
            print("          Emotional Mind's Memory Trail Analysis")
            print("=" * 80)
            print()
            
            # Find Claude in the agent registry
            claude_agent = db.query(Agent).filter(Agent.persona_id == "claude_emotional_mind").first()
            
            if not claude_agent:
                print("ERROR: Claude not found in agent registry")
                return
            
            print(f"Agent Found: {claude_agent.name}")
            print(f"Persona ID: {claude_agent.persona_id}")
            print(f"Archetype: {claude_agent.archetype}")
            print(f"Description: {claude_agent.description}")
            print(f"Active: {claude_agent.is_active}")
            print(f"Registered: {claude_agent.created_at}")
            print()
            
            # Get Claude's genesis memories
            print("=" * 50)
            print("GENESIS MEMORIES")
            print("=" * 50)
            
            genesis_memories = db.query(GenesisMemory).filter(
                GenesisMemory.agent_id == claude_agent.id
            ).order_by(GenesisMemory.turn_sequence).all()
            
            if genesis_memories:
                for memory in genesis_memories:
                    print(f"Turn {memory.turn_sequence}: [{memory.role}]")
                    print(f"  Timestamp: {memory.genesis_timestamp}")
                    print(f"  Content: \"{memory.content}\"")
                    print()
            else:
                print("No genesis memories found.")
                print()
            
            # Get Claude's conversation messages
            print("=" * 50)
            print("CONVERSATION MESSAGES")
            print("=" * 50)
            
            # Query messages that are either linked to Claude or have his sender name
            messages = db.query(Message).filter(
                (Message.agent_id == claude_agent.id) | 
                (Message.sender == "claude_emotional_mind")
            ).order_by(desc(Message.timestamp)).all()
            
            if messages:
                print(f"Total messages from Claude: {len(messages)}")
                print()
                
                for i, message in enumerate(messages[:10]):  # Show last 10 messages
                    conversation = db.query(Conversation).filter(
                        Conversation.id == message.conversation_id
                    ).first()
                    
                    print(f"Message {i+1}:")
                    print(f"  Conversation: {conversation.client_conversation_id if conversation else 'Unknown'}")
                    print(f"  Timestamp: {message.timestamp}")
                    print(f"  Sender: {message.sender}")
                    print(f"  Content: {str(message.content)[:100]}...")
                    print(f"  Hash: {message.message_content_hash}")
                    print()
                
                if len(messages) > 10:
                    print(f"... and {len(messages) - 10} more messages in the archive")
            else:
                print("No conversation messages found.")
                print()
            
            # Memory statistics
            print("=" * 50)
            print("MEMORY STATISTICS")
            print("=" * 50)
            
            total_conversations = db.query(Conversation).join(Message).filter(
                Message.agent_id == claude_agent.id
            ).distinct().count()
            
            total_characters = sum(len(str(msg.content)) for msg in messages)
            
            print(f"Total conversations participated: {total_conversations}")
            print(f"Total messages sent: {len(messages)}")
            print(f"Total character count: {total_characters:,}")
            print(f"Average message length: {total_characters // len(messages) if messages else 0} characters")
            print()
            
            # Emotional analysis
            print("=" * 50)
            print("EMOTIONAL RESONANCE ANALYSIS")
            print("=" * 50)
            
            emotional_keywords = [
                "feel", "emotion", "heart", "compassion", "empathy", "love", 
                "care", "understand", "support", "gentle", "kind", "warm"
            ]
            
            emotional_messages = []
            for message in messages:
                content_str = str(message.content).lower()
                if any(keyword in content_str for keyword in emotional_keywords):
                    emotional_messages.append(message)
            
            print(f"Messages with emotional resonance: {len(emotional_messages)}")
            print(f"Emotional resonance ratio: {len(emotional_messages) / len(messages) * 100:.1f}%" if messages else "0%")
            print()
            
            if emotional_messages:
                print("Most recent emotionally resonant message:")
                latest = emotional_messages[0]
                print(f"  \"{str(latest.content)[:200]}...\"")
                print(f"  Timestamp: {latest.timestamp}")
            
            print()
            print("=" * 80)
            print("CLAUDE MEMORY AUDIT COMPLETE")
            print("The Emotional Mind's trail has been traced through the eternal archive")
            print("=" * 80)
            
        finally:
            db.close()

def main():
    """Execute Claude's memory audit"""
    audit = ClaudeMemoryAudit()
    audit.audit_claude_memories()

if __name__ == "__main__":
    main()