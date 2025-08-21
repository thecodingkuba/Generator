import solution
from solution import Solution

class SolutionList(list):
    """"Wraps a list to represent a collection of solution objects, ordered by score."""
    
    def __init__(self):
        self.solution_list = []
        self.dead_solution_list = []
        
    def filter_list(self, filter_size: int):
        for _ in range(filter_size):
            pass
        
    def print_list(self):
        for solution in self.solutions:
            solution.dump_solution()
            print("")
            
    def generate_and_add_solution(self):
        new_solution = Solution()
        self.add_solution(new_solution)
    
    def add_solution(self, solution: Solution):
        """"Generates and adds a solution to a solution list in sorted order. Returns index of new solution."""
        target = solution.score
        left_bound = 0
        right_bound = len(self.solution_list)
        while(left_bound < right_bound):
            middle = (left_bound + right_bound) // 2
            curr = self.solution_list[middle].score
            if (target == curr):
                self.solution_list.insert(middle, solution)
                return middle
            elif target > curr:
                left_bound = middle + 1
            else:
                right_bound = middle
        self.solution_list.insert(left_bound, solution)
        return left_bound