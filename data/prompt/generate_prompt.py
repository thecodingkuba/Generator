# Template for generating a solution to a given task.
# Usage: generate_prompt.format(task_prompt="Describe a new way to recycle plastic.")
# Variables:
#   {task_prompt} - The task or problem statement for which a solution should be generated.
#   {previous_solutions} - Previously generated solutions to avoid duplicating.

TEMPLATE = """
<system_role>You are a solution generator expert, excelling at generating profitable and optimal solutions for an input task. Keep the solution around a paragraph in length.</system_role>

<user_prompt>
There is a task, and you need to generate an original and unique solution for it. The task is as follows:
<task>
"{task_prompt}"
</task>

{research_section}
{previous_solutions_section}

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

VERSION_TEMPLATE = """
<system_role>You are an expert at giving versions of a solution. Given a solution to a task, give another version to the solution.</system_role>

<user_prompt>
Here is the task, for context.
<task>"{task}"</task>

Here is the solution to the task that you need to generate another version of.
<solution>"{solution}"</solution>

**Output Format Requirements**
Please output only the solution, with no additional comments or explanation.
</user_prompt>
"""
