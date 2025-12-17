# Multi-Step Reasoning AI Agent with Self-Checking

An advanced Generative AI agent designed to solve complex word problems by breaking them into logical steps, executing them, and verifying the output before presenting it to the user.

## 🚀 The Challenge
Standard LLMs often fail at multi-step logic (like complex math or scheduling) because they try to answer all at once. This project implements a **Planner-Executor-Verifier** architecture to ensure high accuracy and reliability.

## 🛠️ Key Features
- **Agentic Workflow**: Uses a dedicated 'Planner' to outline steps and an 'Executor' to process them sequentially.
- **Self-Correction (Verifier)**: A verification layer checks the final answer against the original constraints and triggers retries if errors are detected.
- **Interactive Interface**: Integrated with **Gradio** for a real-time web UI where users can input logic puzzles.
- **JSON Structured Output**: Ensures the agent's response is machine-readable, including the final answer, status, and internal reasoning logs.

## 🧠 Architecture
1. **Planner**: Breaks the input question into a numbered execution plan.
2. **Executor**: Follows the plan exactly to calculate intermediate results.
3. **Verifier**: Acts as a "supervisor" to approve the solution or explain logical inconsistencies for a retry.

## 🧪 Example Problems Solved
- **Time/Logic**: Calculating journey durations (e.g., 14:30 to 18:05).
- **Arithmetic**: Multi-step apple counts with variable multipliers.
- **Constraints**: Finding available meeting slots within specific free-time windows.
