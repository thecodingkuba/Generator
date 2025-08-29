"""Solution class contains one solution and functions to manipulate that solution."""
import json
import os
import src.models.generator as generator
import src.models.judge as judge
         

def save_input(input, output_file):
    """Append result to output file"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(input, ensure_ascii=False) + '\n')     
      
        
class Solution:
    """
    Represents a single generated solution for a given task.

    Attributes:
        task (str, class attribute): The task or problem this solution addresses.
        id (int): Unique identifier for the solution (based on generation order).
        text (str): The generated solution text.
        score (float, optional): The score or rating for the solution.
        metadata (dict, optional): Additional metadata about the solution.
    """
    
    def __init__(self, task: str, count: int, research_dict: dict, criteria_list: list, previous_solutions: list, output_file, metadata=None):
        self.task=task
        self.id=count
        self.research_dict=research_dict
        self.criteria_list=criteria_list
        self.solution = generator.generate_solution(self.task, self.research_dict, self.criteria_list, previous_solutions, output_file)
        self.score = judge.score_solution(self.task, self.solution)
        self.rank = count
        self.dump_solution()     
        
    def dump_solution(self):
        """Dumps solution to solution file."""
        data = {
            "id": self.id,
            "score": self.score,
            "solution": self.solution
        }
        save_input(data, self.output_file)
    
    def print_solution(self):
        """Prints solution to terminal."""
        data = {
            "id": self.id,
            "task": self.task,
            "score": self.score,
            "solution": self.solution
        }
        print(data)
              
    def find_rank(self, solution_list):
        """Return the 1-based rank of solution."""
        return solution_list.index(self) + 1      