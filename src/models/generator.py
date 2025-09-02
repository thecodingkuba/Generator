"""Solution generator LLM to do solution generation tasks"""
import os
import json
import random

import httpx
from openai import OpenAI

from data.prompt.generate_prompt import TEMPLATE, RESEARCH_TEMPLATE, PREVIOUS_SOLUTIONS_TEMPLATE, GOOD_SOLUTIONS_TEMPLATE, BAD_SOLUTIONS_TEMPLATE, CRITERIA_TEMPLATE
from src.models import researcher

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


def generate_research_string(research_dict: dict) -> str:
    """"Builds context for LLM prompt by using output file as reference."""
    lines = [
        f"Query {index + 1}: {query}\nResult: {report}\n" 
        for index, (query, report) in enumerate(research_dict.items())
    ]
    return "".join(lines)
    
    
def generate_research_section(research_dict: dict) -> str:
    """Generates research section context string for LLM prompt."""
    research_string = generate_research_string(research_dict)
    if not research_string:
        return ""
    
    section = RESEARCH_TEMPLATE.format(
        research_string=research_string
    )
    return section


def generate_previous_solutions_section(previous_solutions: list) -> str:
    """"Generates a context string given list of previous solutions."""
    if not previous_solutions:
        return ""
    
    lines = [
        f"Solution {index + 1}: {solution.text}"
        for index, solution in enumerate(previous_solutions)
    ]
    previous_solution_string = "\n".join(lines)
    section = PREVIOUS_SOLUTIONS_TEMPLATE.format(
        previous_solution_string=previous_solution_string
    )
    return section


def generate_good_solutions_section(good_solutions: set) -> str:
    """Generates good solution context string for LLM prompt."""
    if not good_solutions:
        return ""
    
    lines = {
        f"Good solution: {solution.text}"
        for solution in good_solutions
    }
    good_solutions_string = "\n".join(lines)
    
    section = GOOD_SOLUTIONS_TEMPLATE.format(
        good_solutions_string=good_solutions_string
    )
    return section


def generate_bad_solutions_section(bad_solutions: set) -> str:
    """Generates bad solution context string for LLM prompt."""
    if not bad_solutions:
        return ""
    
    lines = {
        f"Bad solution: {solution.text}"
        for solution in bad_solutions
    }
    bad_solutions_string = "\n".join(lines)
    
    section = BAD_SOLUTIONS_TEMPLATE.format(
        bad_solutions_string=bad_solutions_string
    )
    return section


def generate_criteria_section(criteria_list: list) -> str:
    """Generatees criteria section string for LLM prompt"""
    if not criteria_list:
        return ""
    
    lines = [
    f"Criteria {index + 1}: {criteria}"
    for index, criteria in enumerate(criteria_list)
   ]
    criteria_string = "\n".join(lines)
    section = CRITERIA_TEMPLATE.format(
        criteria_string=criteria_string
    )
    return section


def generate_solution(task: str, research_dict, previous_solutions, good_solutions, bad_solutions, criteria_list) -> str:
    """Generate solution to input task"""
    research_section = generate_research_section(research_dict)
    previous_solutions_section = generate_previous_solutions_section(previous_solutions)
    good_solutions_section = generate_good_solutions_section(good_solutions)
    bad_solutions_section = generate_bad_solutions_section(bad_solutions)
    criteria_section = generate_criteria_section(criteria_list)
    prompt = TEMPLATE.format(
        task_prompt=task,
        research_section=research_section,
        previous_solutions_section=previous_solutions_section,
        good_solutions_section=good_solutions_section,
        bad_solutions_section=bad_solutions_section,
        criteria_section=criteria_section
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
    
    
# def generate_versions(task: str, root_solution: str, num_versions=5) -> list:
#     """Takes a core solution and expands it to similar solutions"""
#     versions_list = []
#     prompt = VERSION_TEMPLATE.format(
#         task=task,
#         solution=root_solution
#     )
#     for _ in range(num_versions):
#         versions_list.append(call_model(prompt))
#     return versions_list


def main():
    """Test main that calls the model with a simple task"""
    task = "I need to make sushi for under $5"
    print(generate_solution(task))
    
    
if __name__ == "__main__":
    main()