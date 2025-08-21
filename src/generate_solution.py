"""Main file that user runs to generate a solution for a given task."""

import json
import os

import models.midea_deepresearcher as deepresearcher
import models.deepseek_judge as judge
import models.deepseek_generator as generator
from solution import Solution
from solution_list import SolutionList

NUM_SOLUTIONS = 10
FILTER_SIZE = 4

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
            
    print(f"generating deep research reports now, it will take appromixately {5 * len(deepresearch_queries)} minutes")
    deepresearcher.process_queries(deepresearch_queries)
    print("Research Queries Done Processing")
    
    # ****INITIAL SOLUTION GENERATION****
    solution_list = SolutionList()
    for _ in range(NUM_SOLUTIONS):
        solution_list.generate_and_add_solution()
    solution_list.print_list()
    
    # ****SOLUTION REFINEMENT****

    

if __name__ == "__main__":
    main()
    
    
    