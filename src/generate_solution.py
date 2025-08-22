"""Main file that user runs to generate a solution for a given task."""

import json
import os

import src.models.researcher as researcher
import src.models.judge as judge
import src.models.generator as generator
from src.solution import Solution
from src.solution_list import SolutionList

NUM_SOLUTIONS = 4
FILTER_SIZE = 2

def main():
    """Entry point where user inputs task and gets generated solution."""
    
    # ****SET TASK/PROBLEM****
    task = input("enter task/problem here\n")
    Solution.task = task
    
    # ****RESEARCH QUERIES****
    deepresearch_queries = []
    while True:
        query = input('enter a deep research query here, or type "quit" to continue to the next step\n')
        if query == "quit":
            break
        else:
            deepresearch_queries.append(query)
    if len(deepresearch_queries) > 0:
        print(f"generating deep research reports now, it will take appromixately {5 * len(deepresearch_queries)} minutes")
        researcher.process_queries(deepresearch_queries)
        print("Research Queries Done Processing, now generating solutions...")
    else:
        print("No queries to process, now generating solutions...")
        
    # ****INITIAL SOLUTION GENERATION****
    solution_list = SolutionList()
    for _ in range(NUM_SOLUTIONS):
        solution_list.generate_and_add_solution()
        print(f"Solution generated!")
    print("")
    print("Solution list will print now:")
    solution_list.print_list()
    
    # ****SOLUTION REFINEMENT****

    

if __name__ == "__main__":
    main()


