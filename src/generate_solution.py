import json
import os

import models.midea_deepresearcher as deepresearcher
import models.deepseek_judge as judge
import models.deepseek_generator as generator
from solution import Solution

NUM_SOLUTIONS = 10
RESEARCH_FILE = "research_reports.json"

# ordered from best to worst score
solutions_list = []



def process_queries(deepresearch_queries: list) -> None:
    """Process user list of deepresearch queries, and send to output file."""
    for query in deepresearch_queries:
        deepresearcher.generate_to_file(query)

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
    print("Research Queries Done Processing")
    
    # INITIAL SOLUTION GENERATION
    for _ in range(NUM_SOLUTIONS):
        solutions_list.append()
    
    
    

if __name__ == "__main__":
    main()
    
    
    