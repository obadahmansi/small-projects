
import heapq
import random
import tkinter as tk
import time


# Function to generate a random maze of given size
def generate_maze(size=20, wall_prob=0.2):
    """Generates a random maze with walls."""
    maze = [[' ' for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < wall_prob:
                maze[i][j] = '#'

    start, goal = (0, 0), (size - 1, size - 1)
    maze[start[0]][start[1]] = 'S'
    maze[goal[0]][goal[1]] = 'G'
    return maze, start, goal


# Function to get valid neighbors in the maze
def get_neighbors(position, maze):
    """Returns valid neighbors for a given position."""
    x, y = position
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze) and maze[nx][ny] != '#':
            neighbors.append((nx, ny))
    return neighbors


# Breadth-First Search (BFS) Algorithm
def bfs(maze, start, goal):
    """
    BFS explores all possible moves level by level.
    It guarantees the shortest path in an unweighted maze.
    """
    queue = [(start, [start])]  # Queue stores (current position, path taken)
    visited = set()
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == goal:
            return path  # Return the found path to the goal
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for neighbor in get_neighbors((x, y), maze):
            queue.append((neighbor, path + [neighbor]))
    return None  # No path found


# Depth-First Search (DFS) Algorithm
def dfs(maze, start, goal):
    """
    DFS explores as far as possible in one direction before backtracking.
    It does not guarantee the shortest path but is useful for exploring mazes quickly.
    """
    stack = [(start, [start])]  # Stack stores (current position, path taken)
    visited = set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path  # Return the found path to the goal
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for neighbor in get_neighbors((x, y), maze):
            stack.append((neighbor, path + [neighbor]))
    return None  # No path found


# A* Search Algorithm
def astar(maze, start, goal):
    """
    A* Search uses both cost (steps taken) and a heuristic (Manhattan distance to goal).
    It is more efficient than BFS for large mazes and guarantees the shortest path.
    """
    priority_queue = [(0, start, [start])]  # (cost + heuristic, position, path taken)
    visited = set()
    while priority_queue:
        cost, (x, y), path = heapq.heappop(priority_queue)
        if (x, y) == goal:
            return path  # Return the found path to the goal
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for neighbor in get_neighbors((x, y), maze):
            heuristic = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
            heapq.heappush(priority_queue, (cost + 1 + heuristic, neighbor, path + [neighbor]))
    return None  # No path found


# GUI Functions
def draw_maze():
    """Draws the maze on the canvas."""
    canvas.delete("all")
    for i in range(len(maze)):
        for j in range(len(maze)):
            color = "white"
            if maze[i][j] == '#':
                color = "black"
            elif maze[i][j] == 'S':
                color = "green"
            elif maze[i][j] == 'G':
                color = "red"
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color,
                                    outline="gray")


def animate_path(path):
    """Animates the pathfinding process step by step."""
    if path:
        for (x, y) in path:
            canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="blue",
                                    outline="blue")
            root.update()
            time.sleep(0.1)


def run_algorithm(algorithm):
    """Runs the selected pathfinding algorithm and visualizes the result."""
    global maze, start, goal
    path = None
    if algorithm == 'bfs':
        path = bfs(maze, start, goal)
    elif algorithm == 'dfs':
        path = dfs(maze, start, goal)
    elif algorithm == 'astar':
        path = astar(maze, start, goal)
    draw_maze()
    animate_path(path)


def randomize_maze():
    """Generates a new maze and redraws it."""
    global maze, start, goal
    maze, start, goal = generate_maze()
    draw_maze()


# Initialize GUI
root = tk.Tk()
root.title("Maze Solver")

cell_size = 20
maze, start, goal = generate_maze()
canvas = tk.Canvas(root, width=len(maze) * cell_size, height=len(maze) * cell_size)
canvas.pack()
draw_maze()

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Run BFS", command=lambda: run_algorithm('bfs')).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Run DFS", command=lambda: run_algorithm('dfs')).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Run A*", command=lambda: run_algorithm('astar')).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Randomize Maze", command=randomize_maze).pack(side=tk.LEFT)

root.mainloop()
