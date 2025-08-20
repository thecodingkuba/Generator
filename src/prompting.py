import json
import os
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path

import httpx

# Send reqeust to deepseek V3 model
def deepseek_request(query: str):
    # Set API key directly
    os.environ["DEEPSEEK_API_KEY"] = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
    
    # Or use the default from the API (which may be set in the file)
    client = AIClient()
    
    # Simple test prompt
    response = client.generate("Write a one-sentence bedtime story about a unicorn.")
    print("AI response:", response)
    
