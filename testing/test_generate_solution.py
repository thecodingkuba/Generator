import random
import string
from unittest.mock import patch
import builtins

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.generate_solution as generate_solution

def mock_inputs(inputs):
    """
    Returns a function that mocks the built-in input() to sequentially return values from the provided iterator.

    Args:
        inputs (iterator): An iterator of strings to simulate user input.

    Returns:
        function: A function to be used as a side effect for input() mocking.
    """
    def input_side_effect(prompt=""):
        return next(inputs)
    return input_side_effect

def test_thorough_input():
    """
    Runs a thorough test of the generate_solution.main() interactive loop using a sequence of simulated user inputs.

    The test covers:
        - Task input
        - Skipping deepresearch queries
        - Generating and printing solutions
        - Marking solutions as good and bad
        - Adding and printing criteria
        - Forwarding solutions
        - Handling invalid and edge-case inputs

    Prints any exceptions encountered during execution for debugging.
    """
    inputs = iter([
        "Tell me a funny joke.",           # Task
        "quit",                      # No deepresearch queries (takes too long)
        
        "2",                         # Generate more solutions and print list
        "2",                         
        "1",                         
        
        "3",                         # Mark solutions as good
        "1",                         
        "1",                        
        "2",                      
        "20",                      
        "quit",                      
        
        "6",                         # Print criteria and add criteria
        "5",                         
        "Make the joke about cats.",              
        "Make the joke contain the word meow."    
        "quit",                         

        "2",                         # Generate more solutions
        "1",                         
        
        "4",                         # Mark bad
        "4",                         
        "2",                        
        "0",                         
        "100",                
        "1",         
        "quit",   
        
        "2",                          # Generate more
        "2",
        "quit",
        
        "1",                          # Forward a solution
        "7",
        "1000",
        "7",
        "2"             
    ])
    with patch.object(builtins, 'input', side_effect=mock_inputs(inputs)):
        try:
            generate_solution.main()
        except Exception as e:
            print(f"Test failed with exception: {e}")


if __name__ == "__main__":
    """
    Entry point for running the thorough input test.
    """
    print("Running test_main_random_inputs()")
    test_thorough_input()
