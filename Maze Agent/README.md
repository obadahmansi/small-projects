
# Maze Solver Visualizer 🧭

This Python project allows users to visualize maze solving using three classic pathfinding algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A\* Search**. A simple Tkinter GUI animates each algorithm as it finds a path from start to goal in a randomly generated maze.

---

## 📁 File Contents

- `main.py`: The complete implementation of the maze generator, pathfinding algorithms, and the Tkinter GUI interface.

---

## 🚀 Features

- **Random Maze Generation** with adjustable wall probability.
- Visual animation of:
  - **BFS** – guarantees the shortest path.
  - **DFS** – explores quickly but may not find the shortest path.
  - **A\*** – heuristic-based, efficient and optimal.
- **GUI with Buttons** for algorithm execution and maze randomization.
- **Color Legend**:
  - 🟩 Start
  - 🟥 Goal
  - ⬛ Wall
  - ⬜ Free path
  - 🔵 Path traced by algorithm

---

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Install Tkinter if not already available:
   ```bash
   pip install tk
   ```
3. Run the script:
   ```bash
   python main.py
   ```

---

## 🧠 Algorithms Used

- **BFS (Breadth-First Search)**:
  - Explores neighbors level by level.
  - Guarantees shortest path in an unweighted maze.
- **DFS (Depth-First Search)**:
  - Explores deep into one branch before backtracking.
  - Does **not** guarantee shortest path.
- **A\* (A-Star)**:
  - Uses cost so far + heuristic (Manhattan distance).
  - Efficient and finds the optimal path.

---

## 🧑‍💻 Author

- **Obadah Abdullah Mansi**
---

## 📄 License

This project is open-source and free to use for educational purposes.
