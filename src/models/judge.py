"""Judge LLM functions to do scoring tasks."""

import os
import json
import random

import httpx
from openai import OpenAI

from data.prompt.score_prompt import TEMPLATE

CRITERIA_FILE = "data/input/criteria.json"
DEEPSEEK_API_KEY = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
DEEPSEEK_BASE_URL = "https://aimpapi.midea.com/t-aigc/aimp-deepseek-v3-0324/v1"
client = OpenAI (
        base_url = DEEPSEEK_BASE_URL,
        api_key = DEEPSEEK_API_KEY
    )
 
    
def call_model(prompt: str):
    """"Calls model with given prompt"""
    
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
    
    prompt = TEMPLATE.format(
        task_prompt = task,
        solution = solution,
        criteria_list_string = build_criteria(CRITERIA_FILE)
    )
    return call_model(prompt)


def build_criteria(criteria_file):
    """Builds criteria list into string format to feed into LLM prompt template string."""

    with open(criteria_file, "r") as f:
        criteria_list = json.load(f)
        criteria_list_string = ""
        for criteria in criteria_list:
            criteria_list_string += f"criteria: [{criteria["criteria"]}], description: [{criteria["description"]}] \n"
        return criteria_list_string
    
    
def main():
    """Test main that calls the model with a simple prompt"""
    
    task = "How do I make sushi?"
    solution = "You do not, you lazy pig"
    print(score_solution(task, solution))
    
    
if __name__ == "__main__":
    main()