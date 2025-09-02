SOLUTION_EVAL_PROMPT = """
You are an expert evaluator. Given the following task, a proposed solution, and evaluation criteria, score each dimension and briefly justify your scores.

<Task>
{task_prompt}
</Task>

<Solution>
{solution_text}
</Solution>

<EvaluationCriteria>
{
  "correctness": 0.4,
  "relevance": 0.3,
  "clarity": 0.2,
  "efficiency": 0.1
}
</EvaluationCriteria>

For each dimension:
- Assign a score from 0 to 1.
- Provide a brief justification.

Output your results in this format:
<analysis>
...
</analysis>
<json_output>
{
  "correctness": {"score": 1.0, "justification": "..."},
  "relevance": {"score": 0.8, "justification": "..."},
  "clarity": {"score": 0.9, "justification": "..."},
  "efficiency": {"score": 0.7, "justification": "..."}
}
</json_output>
"""