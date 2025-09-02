TEMPLATE = """
**Task Background**
Given the following task, a proposed solution, and evaluation criteria, score each dimension and briefly justify your scores.

<Task>
{task_prompt}
</Task>

<Solution>
{solution}
</Solution>

<EvaluationCriteria>
{criteria_list}
</EvaluationCriteria>

Instructions:
- For each criterion, analyze how the solution fulfills the requirements.
- Score each criterion on a scale of 0–10 (continuous values).
    * 0–2: Very poor performance.
    * 2–4: Poor performance.
    * 4–6: Average performance.
    * 6–8: Good performance.
    * 8–10: Excellent/outstanding performance.
- Provide a brief, objective analysis for each criterion.
- Output ONLY in the format below. Do not include any unrelated content, introduction, or summary.

<output_format>
{{
    "criterion_name": [
        {{
            "criterion": "[Text of the evaluation criterion]",
            "analysis": "[Brief analysis]",
            "solution_score": [Continuous score 0–10]
        }},
        ...
    ],
    ...
}}
</output_format>
"""