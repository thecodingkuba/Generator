import json
import os

import src.prompting as prompting

NUM_SOLUTIONS = 10
RESEARCH_FILE = "research_reports.json"

solutions_list = []


def generate_solution(prompt: str):
    return "huihihihi"
    
    
def generate_batch(batch_size: int) -> list:
    for _ in batch_size:
        solutions_list.append()
    
    
def save_result(result, output_file):
    """Append result to output file"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False) + '\n')

# prompt all deep research queries

def update_queries():
    for query in research_queries:
        load()
        

def judge_batch():
    for solution in solutions_list:
        grade_solution(problem, solution)
        
        
def grade_solution(problem: str, solution: str) -> float:
    print("place")




# processes initial user list of deepresearch queries
def process_queries(deepresearch_queries: list) -> None:
    for query in deepresearch_queries:
        prompting.deepresearch_request(query)

# main function that generates solution for task
def main():
    # TASK/PROBLEM
    task = input("enter task/problem here\n")
    
    # RESEARCH QUERIES
    deepresearch_queries = []
    while True:
        query = input('enter a deep research query here, or type "quit" to continue to the next step\n')
        if query == "quit":
            break
        else:
            deepresearch_queries.append(query)
    print(f"generating deep research reports now, it will take appromixately {5 * len(deepresearch_queries)} minutes")
    process_queries(deepresearch_queries)    
    
    # INITIAL SOLUTION GENERATION
    
    
    

if __name__ == "__main__":
    main()
    
    
    