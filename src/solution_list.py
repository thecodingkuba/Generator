"""SolutionList class contains one list of solutions and functions to manipulate that list."""
from src.solution import Solution


class SolutionList():
    """"Wraps a list to represent a collection of solution objects, ordered by score."""
    def __init__(self, task, output_file):
        """Initializes solution list and dead solution list."""
        self.task = task
        self.counter = 1
        self.output_file = output_file
        self.solution_list = []
        self.bad_set = set()
        self.good_set = set()
        self.previous_solutions = []
        self.criteria_list = []
        self.research_dict = {}
        
    def print_solution_list(self):
        """Prints out solution list to terminal."""
        for index, solution in enumerate(self.solution_list):
            print(f"Rank {index + 1}: ")
            solution.print_solution()
            print("")
            
    def print_criteria_list(self):
        """Prints out criteria list to terminal."""
        if not self.criteria_list:
            print("No criteria yet.")
        for index, criteria in enumerate(self.criteria_list):
            print(f"Criteria {index + 1}:\n{criteria}")
            
    def add_criteria(self, criteria: str):
        """Adds input criteria to criteria list"""
        self.criteria_list.append(criteria)
        print("Criteria successfully added.")
        
    def mark_bad(self, solution_index: int):
        """Given index, removes solution from main list and puts into dead list."""
        if self.solution_list[solution_index] in self.good_set:
            raise ValueError
        self.bad_set.add(self.solution_list[solution_index])
        self.solution_list.pop(solution_index)
        
    def mark_good(self, solution_index: int):
        """Given index, adds solution to good list (also keeping in main list)"""
        self.good_set.add(self.solution_list[solution_index])
        self.solution_list[solution_index].mark_good()
        
    def add_solution(self, solution: Solution) -> int:
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
        """Generates a new solution and adds it to the solution list and output file."""
        new_solution = Solution(self.task, self.counter, self.research_dict, self.previous_solutions, self.good_set, self.bad_set, self.criteria_list, self.output_file)
        self.add_solution(new_solution)
        self.previous_solutions.append(new_solution)
        self.counter += 1
        print("Solution Generated")
              
    def add_several_solutions(self, num_solutions: int):
        """Generates and adds given number of solutions to solution list."""
        print(f"Generating {num_solutions} solutions...")
        for _ in range(num_solutions):
            self.generate_and_add_solution()
            
    def add_research_report(self, query: str, report: str) -> None:
        """Updates research library to have another report."""
        self.research_dict[query] = report