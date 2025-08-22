"""Judge LLM functions to do scoring tasks."""

import os
import json
import random

import httpx
from openai import OpenAI

from data.prompt.score_prompt import TEMPLATE

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

    
def score_solution(task: str, solution: str) -> float:
    """Returns score (0 to 1) that represents input solution quality to input task."""
    return random.random()


def main():
    """Test main that calls the model with a simple prompt"""
    task = "How do I make sushi?"
    prompt = TEMPLATE.format(
        task_prompt = task
        criteria_list = CRITERIA_LIST
    )
    print(score_solution(task, "DO NOT MAKE SUSHI, YOU ARE SO LAZY"))
    
    
if __name__ == "__main__":
    main()