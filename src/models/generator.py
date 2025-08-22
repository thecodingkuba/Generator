"""Solution generator LLM to do solution generation tasks"""

import os
import json
import random

import httpx
from openai import OpenAI

from data.prompt.generate_prompt import TEMPLATE

DEEPSEEK_API_KEY = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
DEEPSEEK_BASE_URL = "https://aimpapi.midea.com/t-aigc/aimp-deepseek-v3-0324/v1"
client = OpenAI (
        base_url = DEEPSEEK_BASE_URL,
        api_key = DEEPSEEK_API_KEY
    )
    
    
def call_model(prompt: str):
    response = client.chat.completions.create(
    model="/model/Deepseek-V3",
    messages=[
        {"role": "user", "content": prompt}
    ],
    stream=False,
)
    return response.choices[0].message.content


def generate_solution(task: str) -> str:
    """Generate solution to input task"""
    prompt = TEMPLATE.format(
        task_prompt = task
        
    )
    return call_model(prompt)


def main():
    """Test main that calls the model with a simple task"""
    task = "I need to make sushi for under $5"
    print(generate_solution(task))
    
    
if __name__ == "__main__":
    main()