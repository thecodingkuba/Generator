"""Main file that user runs to generate a solution for a given task."""
import json
import os

from src.models import researcher
from src.models import judge
from src.models import generator
from src.solution import Solution
from src.solution_list import SolutionList


NUM_SOLUTIONS = 0


def main():
    """Entry point where user inputs task and gets generated solution."""
    # ****SET TASK/PROBLEM****
    solutions = SolutionList()
    task = input("enter task/problem here\n")
    solutions.task = task
    
    # ****RESEARCH QUERIES****
    deepresearch_queries = []
    while True:
        query = input('enter a deep research query here, or type "quit" to continue to the next step\n')
        if query == "quit":
            break
        else:
            deepresearch_queries.append(query)
    if len(deepresearch_queries) > 0:
        print(f"generating {len(deepresearch_queries)} deep research reports now, it will take appromixately {5 * len(deepresearch_queries)} minutes")
        researcher.process_queries(deepresearch_queries)
        print("Research Queries Done Processing, now generating solutions...")
    else:
        print(f"No queries to process, now generating {NUM_SOLUTIONS} solutions...")
        
    # ****INITIAL SOLUTION GENERATION****
    solutions.add_several_solutions(NUM_SOLUTIONS)
    print("")
    print("Solution list will print now:")
    solutions.print_list()
    
    # ****SOLUTION REFINEMENT****
    
    while True:
        # TODO: FOR SURE Make it so a bad input does not crash everything
        print("""
        Choose from the following:
          1. Mark solution(s) as bad (automatically removes them)
          2. Mark solution(s) as good (to generate better soultions)
          3. Generate more solutions
          4. Select solution to forward (finish program)
          5. Print solution list
          6. Input new criteria for solution.
          """)
        decision = input("Please input the number to select a route\n")
        try:
            match int(decision):
                case 1:
                    while True:
                        solutions.print_list()
                        print("")
                        user_input = input("please input the rank of the solution to mark bad, or type 'quit' to quit\n")
                        if(user_input == "quit"):
                            break
                        try:
                            solutions.kill_solution(int(user_input) - 1)
                        except:
                            print("\nERROR: This is not a valid rank to mark as bad.")
                case 2:
                    while True:
                        solutions.print_list()
                        print("")
                        user_input = input("Please input the rank of the solution to mark good, or type 'quit' to quit:\n")
                        if(user_input == "quit"):
                            break
                        try:
                            solutions.mark_good(int(user_input) - 1)
                        except (ValueError, IndexError):
                            print("\nERROR: This is not a valid rank to mark as good.")
                case 3:
                    try:
                        num_add = int(input("Please input how many solutions to generate\n"))
                        solutions.add_several_solutions(num_add)
                    except ValueError:
                        print("\nERROR: This is not a valid number")
                case 4:
                    try:
                        solutions.print_list()
                        print("")
                        index = (int(input("Please input what rank solution you would like to forward\n"))) - 1
                        
                        solution = solutions.solution_list[index]
                       
                        print("\nYou have found your solution:\n")
                        solution.print_solution()
                        break
                    except (ValueError, IndexError):
                        print("\nERROR: Not a valid rank.")
                case 5:
                    solutions.print_list()
                case 6:
                    while True:
                        user_input = input("\nPlease enter your criteria, or type 'quit' to quit:\n")
                        if(user_input == "quit"):
                            break
                        solutions.add_criteria(user_input)
                case _:
                    print(f"\nERROR: Invalid number. '{decision}' is not a listed option.")
        except ValueError:
            print(f"\nERROR: Invalid input. Please enter a valid number.")
            continue
        except IndexError:
            print(f"\nERROR: Invalid input. Please enter a number within range.")
        
        
if __name__ == "__main__":
    main()


