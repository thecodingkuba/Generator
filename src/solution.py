"""Solution class contains one solution and functions to manipulate that solution."""
import json
import os
import src.models.generator as generator
import src.models.judge as judge
        
        
OUTPUT_FILE = "data/output/solutions.jsonl"

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
    task = None
    counter = 0
    def __init__(self, previous_solutions=None, metadata=None):
        Solution.counter += 1
        self.id = Solution.counter
        self.solution = generator.generate_solution(Solution.task, previous_solutions)
        self.score = judge.score_solution(Solution.task, self.solution)
        self.rank = None
        self.dump_solution()
        
    def dump_solution(self):
        """Dumps solution to solution file."""
        data = {
            "id": self.id,
            "score": self.score,
            "solution": self.solution
        }
        save_input(data, OUTPUT_FILE)
    
    def print_solution(self):
        """Prints solution to terminal."""
        data = {
            "id": self.id,
            "score": self.score,
            "solution": self.solution
        }
        print(data)
        
    def find_rank(self, solution_list):
        """Return the 1-based rank of solution."""
        return solution_list.index(self) + 1      
