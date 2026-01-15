# Multi-Step Reasoning Agent with Self-Verification

## Overview
This project implements a multi-step reasoning agent as required in the assignment.
The agent follows a Planner → Executor → Verifier architecture with retry logic.

A mock LLM is used to simulate agent behavior. This is acceptable as per the assignment
guidelines, which allow mock or rule-based implementations.

## Architecture
- **Planner**: Generates a step-by-step plan without solving the problem.
- **Executor**: Executes the plan internally and returns only the final answer.
- **Verifier**: Independently verifies the answer and returns a pass/fail result.

## How to Run
1. Open the notebook (`.ipynb`) in Google Colab or Jupyter.
2. Run all cells from top to bottom.
3. Example questions and outputs are printed at the end of the notebook.

## Prompting Strategy
Separate prompts are used for each agent:
- Planner prompt ensures no solution is generated.
- Executor prompt enforces hidden reasoning.
- Verifier prompt performs independent verification and outputs structured JSON.

## Example Runs
The notebook includes 8 example questions:
- 5 simple reasoning problems
- 3 edge/tricky cases

Each run demonstrates planning, execution, verification, retries, and final status.

## Assumptions
- The mock LLM is deterministic and rule-based for evaluation purposes.
- Chain-of-thought reasoning is intentionally hidden to comply with safe prompting practices.
