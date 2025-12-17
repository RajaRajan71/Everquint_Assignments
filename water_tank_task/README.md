# Trapping Rainwater Visualizer

An interactive web application that solves and visualizes the "Trapping Rainwater" problem (LeetCode #42).

## 🚀 Overview
This project calculates the total units of water trapped between blocks of varying heights. It includes a dynamic visualization engine that renders the elevation map and water levels using SVG.

## 🛠️ Features
- **Optimal Algorithm**: Uses the pre-calculation method (Max Left & Max Right arrays) to achieve $O(n)$ time complexity.
- **Interactive UI**: Users can input custom block heights (e.g., `0,4,0,0,0,6,0,6,4,0`) and see the results instantly.
- **SVG Visualization**: Dynamically draws the blocks (yellow) and the trapped water (blue) based on the calculated levels.

## 📂 Project Structure
- `index.html`: The main user interface and input system.
- `style.css`: Custom styling for the dashboard and SVG container.
- `water_tank.js`: The core logic for the trapping rainwater algorithm and SVG generation.

## 🧠 Algorithm Logic
The amount of water at any position `i` is determined by:
`Water[i] = min(MaxLeft[i], MaxRight[i]) - Height[i]`.
