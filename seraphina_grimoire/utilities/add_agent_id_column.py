#!/usr/bin/env python3
"""
Manually add agent_id column to messages table
"""

import sys
from pathlib import Path

# Add the CMP backend to the path
cmp_path = Path(__file__).parent.parent.parent / "conversation_memory_project" / "backend"
sys.path.append(str(cmp_path))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://Kryssie6985:58913070Krdpn!!@localhost:5432/cms_db"

def add_agent_id_column():
    """Add agent_id column to messages table"""
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        # Check if column already exists
        result = conn.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'messages' 
            AND column_name = 'agent_id'
        """))
        
        if result.fetchone():
            print("agent_id column already exists")
            return
        
        # Add the column
        print("Adding agent_id column to messages table...")
        conn.execute(text("""
            ALTER TABLE messages 
            ADD COLUMN agent_id INTEGER
        """))
        
        # Add the index
        print("Adding index on agent_id...")
        conn.execute(text("""
            CREATE INDEX ix_messages_agent_id ON messages (agent_id)
        """))
        
        # Add the foreign key constraint
        print("Adding foreign key constraint...")
        conn.execute(text("""
            ALTER TABLE messages 
            ADD CONSTRAINT fk_messages_agent_id 
            FOREIGN KEY (agent_id) REFERENCES agents (id)
        """))
        
        conn.commit()
        print("Successfully added agent_id column to messages table")

if __name__ == "__main__":
    add_agent_id_column()