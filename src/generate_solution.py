"""Main file that user runs to generate a solution for a given task."""

import json
import os

import src.models.researcher as researcher
import src.models.judge as judge
import src.models.generator as generator
from src.solution import Solution
from src.solution_list import SolutionList

NUM_SOLUTIONS = 2
FILTER_SIZE = 1

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
        print(f"No queries to process, now generating {NUM_SOLUTIONS} solutions...")
        
    # ****INITIAL SOLUTION GENERATION****
    solutions = SolutionList()
    solutions.add_several_solutions(NUM_SOLUTIONS)
    print("")
    print("Solution list will print now:")
    solutions.print_list()
    
    # ****SOLUTION REFINEMENT****
    
    while True:
        print("""
              
          Choose from the following:
          1. Mark solution(s) as bad (automatically removes them)
          2. Mark solution(s) as good (to generate better soultions)
          3. Generate more solutions
          4. Select solution to forward
          5. Print solution list
          
          """)
        decision = input("Please input the number to select a route\n")
        match int(decision):
            case 1:
                while True:
                    solutions.print_list()
                    user_input = input("please input the rank of the solution to mark bad, or type 'quit' to quit\n")
                    if(user_input == "quit"):
                        break
                    solutions.kill_solution(int(user_input) - 1)
            case 2:
                while True:
                    solutions.print_list()
                    user_input = input("please input the rank of the solution to mark good, or type 'quit' to quit\n")
                    if(user_input == "quit"):
                        break
                    solutions.mark_good(int(user_input) - 1)
            case 3:
                solutions.add_several_solutions(int(input("please input how many more solutions to generate\n")))
            case 4:
                solutions.print_list()
                index = (int(input("please input what rank solution you would like to forward\n"))) - 1
                print("You have found your solution:\n\n")
                solutions.solution_list[index].print_solution()
                break
            case 5:
                solutions.print_list()
            

if __name__ == "__main__":
    main()


