
# Multi-Step Reasoning Agent for EverQuint Assignments
#applink ---. https://rajarajan71-everquint-assignment-mutli-step-reasoningapp-qxwh7x.streamlit.app/
## 📌 Overview

This repository contains a multi-step reasoning agent implemented in a notebook (`.ipynb`) as required in the assignment.

The agent follows a Planner → Executor → Verifier architecture with retry and self-verification logic.

A **mock LLM** is used to simulate agent behaviour in a realistic way as allowed by the assignment guidelines.

---

## 🧠 Architecture

1. **Planner**  
   - Generates a question-specific plan without solving the problem.

2. **Executor**  
   - Follows the plan step-by-step, reasoning internally, and returns only the final actionable answer.

3. **Verifier**  
   - Independently verifies the solution and returns a structured pass/fail response.

---

## 🚀 How to Run

1. Open the `Mutli_step_reasoning.ipynb` file in Google Colab or Jupyter Notebook.
2. Run all cells from top to bottom.
3. Example questions and outputs are printed at the end as part of the test suite.

---

## 📝 Prompting Strategy

Separate prompts are used for each agent:
- **Planner**: Structured plan generation with no solution content.
- **Executor**: Internal reasoning only, ensures outputs comply with plan.
- **Verifier**: Independent validation and JSON output.

Chain-of-thought is intentionally hidden to meet safe prompting requirements.

---

## 📊 Example Runs

The notebook includes **8 questions**:
- 5 easy reasoning problems
- 3 tricky edge cases

Each question output includes:
- Final answer
- Status (success/failed)
- Metadata (plan, verification logs, retries)

---

## 📌 Assumptions

- A mock rule-based LLM is used for deterministic behavior and simplicity.
- The reasoning logic follows the required multi-step design and is swappable with any real LLM.

