"""Researcher LLM to call deepresearch API and return/store data."""
import json
import os
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path

import httpx

import src.solution_list

# API Setup
BASE_URL = "https://aimpapi.midea.com/t-aigc/airc-deepresearch-sit/"
AUTH_TOKEN = "msk-d60011d8a6905bd6b8d72cb77f847d978e387c253266a1dc5beb1c60f8fddf9b"
ASSISTANT_ID = "xm_deep_search"
MIP = "liuchen21"
text_request_template = {
    "request_id": f"test_{uuid.uuid4().hex}",
    "assistant_id": "xm_deep_search",
    "content": "ask something!",
    "metadata": {},
    "context": {}
} 
        
        
def call_model(query_text, thread_id=None) -> str:
    """Call Midea API with the working configuration"""
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {AUTH_TOKEN}"}
    
    # Use working endpoint
    api = BASE_URL.rstrip("/") + f"/v1/threads/{thread_id or uuid.uuid4().hex}/runs_stream"
    
    # Prepare request data
    data = text_request_template.copy()
    data["assistant_id"] = ASSISTANT_ID
    data["content"] = query_text
    data["metadata"]["mip"] = MIP
    data["request_id"] = f"batch_{uuid.uuid4().hex}"
    
    try:
        timeout = httpx.Timeout(6000)  # 100 minutes timeout for complex queries
        with httpx.Client(timeout=timeout) as client:
            resp = client.request("post", api, json=data, headers=headers)
            resp.raise_for_status()
            
            response_text = resp.text
            
            # Parse streaming format to extract content
            content_pieces = []
            final_content = None
            
            for line in response_text.split('\n'):
                if line.strip() and line.startswith('data: '):
                    try:
                        json_str = line[6:]  # Remove 'data: ' prefix
                        chunk_data = json.loads(json_str)
                        
                        if 'content' in chunk_data:
                            content = chunk_data['content']
                            if isinstance(content, str) and content.strip():
                                content_pieces.append(content)
                            elif isinstance(content, list) and len(content) > 0:
                                for item in content:
                                    if item.get('type') == 'text':
                                        final_content = item.get('text', '')
                                        break
                    except json.JSONDecodeError:
                        continue
            
            # Return the best content we found
            if final_content:
                return final_content
            elif content_pieces:
                return ''.join(content_pieces)
            else:
                return None
                
    except Exception as e:
        print(f"Error calling API: {e}")
        return None
    
    
def save_report(query, result, output_file) -> None:
    """Append result to output file"""
    report_data = {
        "query": query,
        "report": result
    }
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(report_data, ensure_ascii=False) + '\n')


def process_queries(deepresearch_queries: list, output_file: str, solution_list: "src.SolutionList") -> None:
    """Process user list of deepresearch queries, and send to output file."""
    for index, query in enumerate(deepresearch_queries):
        report = call_model(query)
        save_report(query, report, output_file)
        solution_list.add_research_report(query, report)
        print(f"Report {index + 1} generated.")


def main():
    """Test API with simple model call"""
    prompt = "what is a good app that can track my goals in a to do list format"
    print(call_model(prompt))
    
    
if __name__ == "__main__":
    main()
