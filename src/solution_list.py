from src.solution import Solution

class SolutionList(list):
    """"Wraps a list to represent a collection of solution objects, ordered by score."""
    
    def __init__(self):
        """Initializes solution list and dead solution list."""
        self.solution_list = []
        self.dead_solution_list = []
        
    # def filter_list(self, filter_size: int):
    #     for _ in range(filter_size):
    #         pass
        
    def print_list(self):
        """Prints out solution list to terminal."""
        rank_counter = 0
        for index, solution in enumerate(self.solution_list):
            rank = index + 1
            print(f"{rank}: ")
            solution.print_solution()
            
    def generate_and_add_solution(self):
        """Generates a new solution and adds it to the solution list."""
        new_solution = Solution()
        self.add_solution(new_solution)
    
    def add_solution(self, solution: Solution):
        """"Inserts a given solution to the solution list in sorted order. Returns index of new solution."""
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