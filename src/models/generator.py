"""Solution generator LLM to do solution generation tasks"""

import os
import json
import random

import httpx
from openai import OpenAI

from data.prompt.generate_prompt import TEMPLATE
from data.prompt.generate_prompt import VERSION_TEMPLATE

DEEPSEEK_API_KEY = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
DEEPSEEK_BASE_URL = "https://aimpapi.midea.com/t-aigc/aimp-deepseek-v3-0324/v1"
client = OpenAI (
        base_url = DEEPSEEK_BASE_URL,
        api_key = DEEPSEEK_API_KEY
    )
    
    
def call_model(prompt: str, temperature=0.7, top_p=0.9, frequency_penalty=0.5, presence_penalty=0.3):
    """"Calls model with given prompt"""
    response = client.chat.completions.create(
        model="/model/Deepseek-V3",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=False,
    )
    return response.choices[0].message.content

def generate_previous_solutions_string(previous_solutions: list):
    """"Generates a context string given list of previous solutions."""
    text = ""
    for index, solution in enumerate(previous_solutions):
        text += f"Solution {index + 1}: solution\n"
    return text

def generate_solution(task: str, previous_solutions=None) -> str:
    """Generate solution to input task"""
    previous_solutions_string = generate_previous_solutions_string(previous_solutions)
    prompt = TEMPLATE.format(
        task_prompt=task,
        previous_solutions=previous_solutions_string
    )
    
    # Use random parameters for diversity
    temperature = random.uniform(0.7, 1.1)  # Higher temperature for more diversity
    top_p = random.uniform(0.85, 0.98)      # Higher top_p for broader token selection
    freq_penalty = random.uniform(0.3, 0.7) # Reduce repetition of phrases
    pres_penalty = random.uniform(0.2, 0.5) # Encourage new topics
    
    return call_model(
        prompt,
        temperature=temperature,
        top_p=top_p, 
        frequency_penalty=freq_penalty,
        presence_penalty=pres_penalty
    )
    
def generate_versions(task: str, root_solution: str, num_versions=5) -> list:
    """Takes a core solution and expands it to similar solutions"""
    versions_list = []
    prompt = VERSION_TEMPLATE.format(
        task=task,
        solution=root_solution
    )
    for _ in range(num_versions):
        versions_list.append(call_model(prompt))
    return versions_list


def main():
    """Test main that calls the model with a simple task"""
    task = "I need to make sushi for under $5"
    print(generate_solution(task))
    
    
if __name__ == "__main__":
    main()