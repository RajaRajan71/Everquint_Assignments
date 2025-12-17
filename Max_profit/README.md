# Max Profit Land Development Optimizer

A data-driven optimization tool that solves a complex resource-allocation problem for land development using Dynamic Programming.

## 🚀 The Challenge
Given a total time constraint (n), the goal is to find the optimal mix of properties (Theatres, Pubs, and Commercial Parks) to maximize total earnings. Each property has a different build time and a different earning rate per unit of time operational.

## 🛠️ Features
- **Streamlit Dashboard**: A user-friendly web interface to test various time constraints.
- **Dynamic Programming (DP) Engine**: An $O(n)$ algorithm that determines the most profitable building sequence.
- **Data Visualization**: Real-time bar charts showing the property distribution for the calculated solution.

## 🧠 The Logic
The value of each building depends on its **Completion Time**. 
- **Profit = Earning Rate × (Total Time - Completion Time)**
The algorithm must decide the sequence of buildings because a building completed earlier earns more than the same building completed later.

## 📊 Results
Successfully passes all interview test cases:
- Time Unit 7: $3,000 (1 Theatre)
- Time Unit 8: $4,500 (1 Theatre)
- Time Unit 13: $16,500 (2 Theatres)
