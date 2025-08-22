# Template for generating a solution to a given task.
# Usage: generate_prompt.format(task_prompt="Describe a new way to recycle plastic.")
# Variables:
#   {task_prompt} - The task or problem statement for which a solution should be generated.

TEMPLATE = """
<system_role>You are a solution generator expert, excelling at generating profitable and optimal solutions for an input task. Keep the solution around a paragraph in length.</system_role>

<user_prompt>
There is a task, and you need to generate the best solution for it. The task is as follows:
<task>
"{task_prompt}"
</task>

**Output Format Requirements**
Please make sure you **strictly** follow the following '<output_format>' template:

<output_format>
{"Solution": [full solution here]}
</output_format>

Now, proceed to generate the best solution you can, and make sure you follow the output format without adding any additional comments or explanation.
</user_prompt>
"""