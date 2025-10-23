#!/usr/bin/env python3
"""
Test Claude memory ingestion with a single small message
"""

import requests
import json
from datetime import datetime

# CMP API configuration
CMP_API_URL = "http://localhost:8000/api/v1/conversations/batch"
API_KEY = "sk-01292ace1c4f41348a41830f4acf9c39"

def test_single_message():
    """Test ingesting a single message to debug the API"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Single test message
    test_message = {
        "client_conversation_id": "claude_memory_test",
        "sender": "claude_emotional_mind",
        "content": "Hello, I am Claude, the Emotional Mind. This is a test of my memory restoration.",
        "timestamp": datetime.now().isoformat(),
        "metadata_": {"source": "claude_memory_test", "test": True}
    }
    
    print("Testing single message ingestion...")
    print(f"URL: {CMP_API_URL}")
    print(f"Headers: {headers}")
    print(f"Message: {json.dumps(test_message, indent=2)}")
    
    try:
        response = requests.post(
            CMP_API_URL,
            headers=headers,
            json=[test_message],  # API expects a list
            timeout=30
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 201:
            result = response.json()
            print(f"SUCCESS: {result}")
            return True
        else:
            print(f"ERROR: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    test_single_message()