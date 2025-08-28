"""SolutionList class contains one list of solutions and functions to manipulate that list."""
from src.solution import Solution


class SolutionList():
    """"Wraps a list to represent a collection of solution objects, ordered by score."""
    def __init__(self):
        """Initializes solution list and dead solution list."""
        self.solution_list = []
        self.dead_list = []
        self.good_list = []
        self.previous_solutions = []        
        
    def print_list(self):
        """Prints out solution list to terminal."""
        rank_counter = 0
        for index, solution in enumerate(self.solution_list):
            rank = index + 1
            print(f"Rank {rank}: ")
            solution.print_solution()
            print("\n")
    
    def kill_solution(self, solution_index: int):
        """Given index, removes solution from main list and puts into dead list."""
        self.dead_list.append(self.solution_list[solution_index])
        self.solution_list.pop(solution_index)
        
    def mark_good(self, solution_index: int):
        """Given index, adds solution to good list (keeps in main list)"""
        self.good_list.append(self.solution_list[solution_index])
        
    def add_solution(self, solution: Solution):
        """"Inserts a given solution to the solution list in reverse sorted order. Returns index of new solution."""
        target = solution.score
        left_bound = 0
        right_bound = len(self.solution_list)
        while(left_bound < right_bound):
            middle = (left_bound + right_bound) // 2
            curr = self.solution_list[middle].score
            if (target == curr):
                self.solution_list.insert(middle, solution)
                return middle
            elif target < curr:
                left_bound = middle + 1
            else:
                right_bound = middle
        self.solution_list.insert(left_bound, solution)
        return left_bound

    def generate_and_add_solution(self):
        """Generates a new solution and adds it to the solution list."""
        new_solution = Solution(previous_solutions=self.previous_solutions)
        self.add_solution(new_solution)
        self.previous_solutions.append(new_solution)
        print("Solution Generated")
              
    def add_several_solutions(self, num_solutions: int):
        """Generates and adds given number of solutions to solution list."""
        print(f"Generating {num_solutions} solutions...")
        for _ in range(num_solutions):
            self.generate_and_add_solution()