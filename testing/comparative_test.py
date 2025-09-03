from unittest.mock import patch
import builtins

import sys
import os

import src.generate_solution as generate_solution


inputs = [
    # 1. Indoor air quality improvement
    (
        "Suggest an innovative method for improving indoor air quality using air conditioning systems.",
        [
            "What are the latest technologies for air purification in HVAC systems?",
            "Are there recent advancements in smart sensors for monitoring indoor air quality"
        ],
        [
            "Can be implemented in existing AC systems without major hardware changes",
            "Does not increase total energy consumption by more than 10%"
        ]
    ),
    # 2. AC performance in high humidity
    (
        "Develop a plan to optimize AC performance in regions with high humidity.",
        [
            "What are the main challenges faced by air conditioning systems in high humidity environments?"
        ],
        [
            "Prevents mold and mildew growth in AC units and ductwork",
            "Complies with local and international air quality and efficiency standards"
        ]
    ),
    # 3. Air filtration for allergy sufferers
    (
        "Identify the most effective air filtration technologies for allergy sufferers.",
        [
            "What air filtration technologies are proven to remove common allergens such as pollen, dust mites, and pet dander?"
        ],
        [
            "Safe for continuous use in homes with children, elderly, and pets"
        ]
    ),
    # 4. Anti corrosion coating for AC condensers
    (
        "Select the top-rated anti corrosion coating for outdoor AC condensers.",
        [
            "How do different coatings perform in coastal and high-humidity environments?"
        ],
        [
            "Are there industry standards or certifications for corrosion protection in HVAC equipment?"
        ]
    ),
    # 5. Energy-efficient AC configuration for office buildings
    (
        "Determine the most energy-efficient air conditioning configuration for a multi story office building, considering different unit types, placements, and control strategies.",
        [
            "What are the comparative energy efficiencies of central, split, and VRF AC systems in office buildings?",
            "How does AC unit placement affect overall energy consumption?",
            "What control strategies (e.g., zoning, smart thermostats) optimize energy use in multi-story buildings?"
        ],
        [
            "Complies with local building codes and energy standards",
            "Can be implemented without major structural changes"
        ]
    ),
    # 6. Dietary interventions for diabetes
    (
        "Identify the best dietary interventions for managing diabetes.",
        [
            "What dietary patterns have shown the greatest efficacy in controlling blood glucose?",
            "Are there recent clinical trials comparing low-carb, Mediterranean, and plant-based diets for diabetes?",
            "What are the long-term health outcomes of popular diabetes diets?"
        ],
        [
            "Intervention must be supported by peer-reviewed clinical studies",
            "Safe for long-term use",
            "Affordable and accessible for most patients"
        ]
    ),
    # 7. Cybersecurity practices for small business
    (
        "Determine the most optimal cybersecurity practices for a small business.",
        [
            "What cybersecurity measures are most effective for small businesses?",
            "What are the latest threats targeting small business IT systems?"
        ],
        [
            "Practices must be cost-effective and scalable",
            "Complies with relevant data protection regulations",
            "Demonstrated effectiveness against common cyber threats"
        ]
    ),
    # 8. Crop yield strategy for drought-prone area
    (
        "Craft a strategy to increase crop yields in a drought-prone area.",
        [
            "What irrigation technologies are most effective in drought conditions?",
            "Are there drought-resistant crop varieties suitable for the region?",
            "What soil management practices improve water retention?"
        ],
        [
            "Strategy must increase yields by at least 15% under drought conditions",
            "Sustainable and environmentally friendly"
        ]
    ),
    # 9. Mental health intervention for teenagers
    (
        "Create a mental health intervention plan for teenagers.",
        [
            "What mental health interventions have proven effective for adolescents?",
            "What are the best practices for engaging teenagers in mental health programs?"
        ],
        [
            "Intervention must be evidence-based",
            "Accessible in school and community settings"
        ]
    ),
    # 10. Remote monitoring system for AC units
    (
        "Design a remote monitoring system for AC unit performance in large commercial buildings.",
        [
            "What sensors and technologies are most effective for monitoring AC performance remotely?",
            "How can data from multiple AC units be aggregated and analyzed for predictive maintenance?",
            "Are there recent advancements in wireless communication for HVAC monitoring?"
        ],
        [
            "System must provide real-time alerts for performance issues",
            "Compatible with existing commercial AC units",
            "Installation cost does not exceed $2000 per building"
        ]
    )
]
  
  
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


def single_run(data: tuple[str, list[str], list[str]]):
    """
        Tests a simple example with deepresearch context.
        Tuple Structure: (<Task String>, <Research Query List>, <Criteria List>)
    """
    inputs = iter ([
        data[0],           # Task
        
        
        *data[1],           # Deepresearch Queries
        "quit",
        
                                      
        "5",               # Add criteria     
        *data[2],              
        "quit",                         


        "2",               # Generate solutions
        "4",                         
        
        
        "3",               # Mark good
        "1",                         
        "2",                        
        "quit",  
        
        
        "4",               # Mark bad
        "4",                         
        "5",                        
        "quit",   
        
        "2",               # Generate solutions
        "2",
        "quit",
        
        "7",               # Forward a solution
        "2",       
    ])
    with patch.object(builtins, 'input', side_effect=mock_inputs(inputs)):
        try:
            generate_solution.main()
        except Exception as e:
            print(f"Test failed with exception: {e}")
    
    
def multiple_runs(inputs: list[tuple[str, list[str], list[str]]]):
    """Takes list of tuples to perform several runs. One with and one without research context for each."""
    for index, input in enumerate(inputs):
        single_run(input)
        input_no_research = (input[0], [], input[2])
        single_run(input_no_research)
        print(f"Test Task {index + 1} out of {len(inputs)} complete.")
    
        
def main():
    """Takes list of inputs to do several runs."""
    multiple_runs(inputs)
    
    
if __name__ == "__main__":
    main()