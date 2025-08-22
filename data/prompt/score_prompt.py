# Template for scoring a solution to a given task using specific evaluation criteria.
#
# Usage:
#   score_prompt.format(task_prompt="Describe a new way to recycle plastic.", criteria_list="...criteria...")
#
# Variables:
#   {task_prompt}    - The task or problem statement being evaluated.
#   {criteria_list}  - The list of evaluation criteria (as a string) to judge the solution.
#
# The LLM is instructed to output a JSON object in the specified format, with no extra comments.

TEMPLATE = """
<system_role>You are a strict and objective solution evaluation expert, excelling at using specific criteria to thoroughly judge the quality of a solution to a task.</system_role>

<user_prompt>
**Task Background**
There is a task, and you need to evaluate a solution to the given task. The task is as follows:
<task>
{task_prompt}
</task>

**Evaluation Criteria**
You will need to evaluate the solution based on the following evaluation criteria list. Each criteria includes an explanation, so understand carefully.
The criteria list is as follows:
<criteria_list>
{criteria_list}
</criteria_list>

<Instruction>
**Your Task**
Score the solution from 0 to 1, considering the given evaluation criteria. The solution is as follows:
<solution>
{solution}
</solution>

Please output **only** the score as a single number between 0 and 1. Do not include any other text, explanation, or formatting.
</Instruction>
</user_prompt>
"""