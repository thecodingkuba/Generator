"""Main file that user runs to generate a solution for a given task."""
import json
import os
from datetime import datetime
import re 

from src.models import researcher
from src.models import judge
from src.models import generator
from src.solution import Solution
from src.solution_list import SolutionList

NUM_SOLUTIONS = 2


def create_session_base_filepath(task: str) -> str:
    """Builds a valid filename based off the datetime and given task."""
    task = task.lower()
    task = re.sub(r'[^a-z0-9_]+', '_', task)
    task = task.strip('_')
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    filename = f"{task}_{timestamp}.jsonl"
    return filename


def main():
    """Entry point where user inputs task and gets generated solution."""
    # ****SET TASK/PROBLEM****
    task = input("Enter task/problem here:\n")
    print("")
    base_path = create_session_base_filepath(task)
    solution_file = os.path.join("data", "output", "solutions", base_path)
    solutions = SolutionList(task, solution_file)
    
    
    # ****RESEARCH QUERIES****
    research_file = os.path.join("data", "output", "research", base_path)
    deepresearch_queries = []
    while True:
        query = input('Enter a deep research query here, or type "quit" to continue to the next step:\n')
        if query == "quit":
            print("")
            break
        else:
            print("")
            deepresearch_queries.append(query)
    if len(deepresearch_queries) > 0:
        print(f"Generating {len(deepresearch_queries)} deep research reports now, it will take appromixately {5 * len(deepresearch_queries)} minutes.")
        researcher.process_queries(deepresearch_queries, research_file, solutions)
        print("Research Queries Done Processing!")
    else:
        print(f"No queries to process.")
        
    # ****INITIAL SOLUTION GENERATION****
    solutions.add_several_solutions(NUM_SOLUTIONS)
    print("")
    print("Solution list will print now:")
    solutions.print_solution_list()
    
    # ****SOLUTION REFINEMENT****
    
    while True:
        print("""
        Choose from the following:
          1. Print solution list
          2. Generate more solutions
          3. Mark solution(s) as good (to generate better soultions)
          4. Mark solution(s) as bad (automatically removes them)
          5. Input new criteria for solution
          6. Print criteria list
          7. Select solution to forward (finish program)
          """)
        decision = input("Please input the number to select a route:\n")
        try:
            match int(decision):
                case 1:
                    solutions.print_solution_list()
                case 2:
                    try:
                        num_add = int(input("Please input how many solutions to generate\n"))
                        solutions.add_several_solutions(num_add)
                    except ValueError:
                        print("\nERROR: This is not a valid number")
                case 3:
                    while True:
                        solutions.print_solution_list()
                        print("")
                        user_input = input("Please input the rank of the solution to mark good, or type 'quit' to quit:\n")
                        if(user_input == "quit"):
                            break
                        try:
                            solutions.mark_good(int(user_input) - 1)
                        except (ValueError, IndexError):
                            print("\nERROR: This is not a valid rank to mark as good.")
                case 4:
                    while True:
                        solutions.print_solution_list()
                        print("")
                        user_input = input("Please input the rank of the solution to mark bad, or type 'quit' to quit\n")
                        if(user_input == "quit"):
                            break
                        try:
                            solutions.mark_bad(int(user_input) - 1)
                        except (ValueError, IndexError):
                            print("\nERROR: This is not a valid rank to mark as bad.")
                case 5:
                    while True:
                        user_input = input("\nPlease enter your criteria, or type 'quit' to quit:\n")
                        if(user_input == "quit"):
                            break
                        solutions.add_criteria(user_input)
                case 6:
                    solutions.print_criteria_list()
                case 7:
                    try:
                        solutions.print_solution_list()
                        print("")
                        index = (int(input("Please input what rank solution you would like to forward\n"))) - 1
                        
                        solution = solutions.solution_list[index]
                       
                        print("\nYou have found your solution:\n")
                        solution.print_solution()
                        return
                    except (ValueError, IndexError):
                        print("\nERROR: Not a valid rank.")
                case _:
                    print(f"\nERROR: Invalid number. '{decision}' is not a listed option.")
        except ValueError:
            print(f"\nERROR: Invalid input. Please enter a valid number.")
            continue
        
        
if __name__ == "__main__":
    main()


