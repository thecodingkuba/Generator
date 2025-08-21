import json
import os
import models.deepseek_generator as generator
import models.deepseek_judge as judge


        
OUTPUT_FILE = "data/solution_file.json"



def save_input(input, output_file):
    """Append result to output file"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(input, ensure_ascii=False) + '\n')
        

        
class Solution:
    """
    Represents a single generated solution for a given task.

    Attributes:
        id (int): Unique identifier for the solution.
        task (str): The task or problem this solution addresses.
        text (str): The generated solution text.
        score (float, optional): The score or rating for the solution.
        metadata (dict, optional): Additional metadata about the solution.
    """
    task = None
    counter = 0
    def __init__(self, metadata=None):
        Solution.counter += 1
        self.id = Solution.counter
        self.solution = generator.create_solution(task)
        self.score = judge.score_solution(self.task, self.solution)
        self.rank = None
        
    def dump_solution(self):
        data = {
            "id": self.id,
            "score": self.score,
            "solution": self.solution
        }
        save_input(data, OUTPUT_FILE)
        
    def find_rank(self, solution_list):
        """Return the 1-based rank of solution."""
        return solution_list.index(self) + 1      
    
    def filter_out(filter_size):