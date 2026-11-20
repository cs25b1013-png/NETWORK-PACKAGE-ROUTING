# Network Packet Routing Using Search Algorithms

Implementation of various uninformed, informed, local search, and constraint satisfaction algorithms in Python to find optimal paths for routing packets across a network of routers.

## Algorithms Included

### Uninformed Search
- **`bfs.py`** – Breadth-First Search (finds the path with the fewest hops)
- **`dfs.py`** – Depth-First Search
- **`iddfs.py`** – Iterative Deepening Depth-First Search
- **`uniform_search.py`** – Uniform Cost Search (finds the lowest-cost path)

### Informed Search
- **`a_star.py`** – A* Search (uses path cost + heuristic estimate)
- **`greedy_best.py`** – Greedy Best-First Search

### Local Search
- **`hill_climbing.py`** – Hill Climbing
- **`simulated_annealing.py`** – Simulated Annealing

### Constraint Satisfaction (CSP)
- **`backtracking.py`** – Backtracking Search for valid route constraints
- **`ac3.py`** – Arc Consistency 3 (AC-3) for pruning invalid network paths

## Project Structure
```text
.
├── a_star.py
├── ac3.py
├── backtracking.py
├── bfs.py
├── dfs.py
├── greedy_best.py
├── hill_climbing.py
├── iddfs.py
├── simulated_annealing.py
├── uniform_search.py
└── README.md
