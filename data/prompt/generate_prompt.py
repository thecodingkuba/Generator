# Template for generating a solution to a given task.
# Usage: TEMPLATE.format(
#     task_prompt="Describe a new way to recycle plastic.",
#     research_section=...,
#     previous_solutions_section=...,
#     good_solutions_section=...,
#     bad_solutions_section=...,
#     criteria_section=...
# )
# Variables:
#   {task_prompt} - The task or problem statement for which a solution should be generated.
#   {research_section} - Optional research context to guide the solution.
#   {previous_solutions_section} - Section listing previous solutions to avoid duplication.
#   {good_solutions_section} - Section listing examples of good solutions.
#   {bad_solutions_section} - Section listing examples of bad solutions.
#   {criteria_section} - Section listing user-provided criteria

TEMPLATE = """
<system_role>You are a solution generator expert, excelling at generating profitable and optimal solutions for an input task. Keep the solution around a paragraph in length.</system_role>

<user_prompt>
There is a task, and you need to generate an original and unique solution for it. The task is as follows:
<task>
"{task_prompt}"
</task>

{research_section}
{previous_solutions_section}
{good_solutions_section}
{bad_solutions_section}
{criteria_section}

Remember, your task is:
<task>
"{task_prompt}"
</task>

**Output Format Requirements**
Please output only the solution, with no additional comments or explanation.
</user_prompt>
"""


RESEARCH_TEMPLATE = """
Here is some research context that should guide your solution:
<research_context>
{research_string}
</research_context>
"""


PREVIOUS_SOLUTIONS_TEMPLATE = """
Make sure it is distinct from the following previously generated solutions:
<previous_solutions>
{previous_solution_string}
</previous_solutions>
"""


GOOD_SOLUTIONS_TEMPLATE = """
Here are some of the previous solutions that have been deemed "good":
<good_solutions>
{good_solutions_string}
</good_solutions>
"""


BAD_SOLUTIONS_TEMPLATE = """"
Here are some of the previous solutions that have been deemed "bad":
<bad_solutions>
{bad_solutions_string}
</bad_solutions>
"""


CRITERIA_TEMPLATE = """
The user has given some criteria you should follow. Here it is:
<user_criteria>
{criteria_string}
</user_criteria>
"""


# VERSION_TEMPLATE = """
# <system_role>You are an expert at giving versions of a solution. Given a solution to a task, give another version to the solution.</system_role>

# <user_prompt>
# Here is the task, for context.
# <task>"{task}"</task>

# Here is the solution to the task that you need to generate another version of.
# <solution>"{solution}"</solution>

# **Output Format Requirements**
# Please output only the solution, with no additional comments or explanation.
# </user_prompt>
# """
