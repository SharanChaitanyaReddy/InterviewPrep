# Month 02 - Week 04 Plan – FAANG Prep

## 1. Motivation & Focus Reminder
- This 90-minute daily preparation is **non-negotiable**.
- Remember why you are doing this: building skills for **FAANG / top MNC**, mastering **DSA**, **system design**, and **AI fundamentals**.
- Focus on **small wins every day**, not the entire roadmap at once.
- Keep distractions away: phone on silent, no YouTube rabbit holes.

---

Week 8 – Month 2: Weighted Graphs & Advanced Graph Patterns

Objective:
Understand weighted graphs, shortest paths, and advanced traversal patterns. Apply BFS/DFS knowledge (Week 7) to real-world problems like routing and optimization.

Folder structure for code:

Code/python/week-08/
├── day-01-weighted-graphs/
├── day-02-dijkstra-algorithm/
├── day-03-bellman-ford-algorithm/
├── day-04-prims-mst/
└── day-05-graph-problems-advanced/

Day 1: Weighted Graphs – Introduction

Topics:

Weighted vs unweighted graphs

Real-world examples: maps, network latency, cost optimization

Graph representation with weights (adjacency list with weights, adjacency matrix)

Time/space trade-offs

Dependencies: Week 7 (Graph basics & traversal), Python dict/list (Week 2)

Code Folder: Code/python/week-08/day-01-weighted-graphs/
Documentation Link: 04-Advanced-DSA/graphs/weighted-graphs.md

Hands-on Coding:

Implement weighted graph class

Add edges with weights

Print adjacency list/matrix with weights

Day 2: Dijkstra’s Algorithm

Topics:

Shortest path for weighted graphs (non-negative edges)

Greedy approach concept

Priority queue / min-heap usage

Time/space complexity analysis

Dependencies: Day 1 weighted graphs, heap (Week 3), BFS template (Week 7)

Code Folder: Code/python/week-08/day-02-dijkstra-algorithm/
Documentation Link: 04-Advanced-DSA/graphs/shortest-path.md

Hands-on Coding:

Implement Dijkstra’s algorithm

Track distance array and parent nodes

Solve 2–3 example problems with explanations

Day 3: Bellman-Ford Algorithm

Topics:

Shortest path with negative weights

Difference between Dijkstra & Bellman-Ford

Detect negative cycles

Dynamic programming relation to Bellman-Ford

Dependencies: Day 2 Dijkstra, DP basics (Week 6)

Code Folder: Code/python/week-08/day-03-bellman-ford-algorithm/
Documentation Link: 04-Advanced-DSA/graphs/shortest-path.md

Hands-on Coding:

Implement Bellman-Ford algorithm

Test negative weight edges

Annotate iterations, time/space complexity

Day 4: Minimum Spanning Trees (Prim’s & Kruskal’s)

Topics:

MST concept: connect all nodes with minimum cost

Prim’s algorithm (priority queue)

Kruskal’s algorithm (union-find / disjoint sets)

Real-world analogy: network design, circuit optimization

Dependencies: Weighted graphs (Day 1), Union-Find (Week 6), Heap (Week 3)

Code Folder: Code/python/week-08/day-04-prims-mst/
Documentation Link: 04-Advanced-DSA/graphs/mst.md

Hands-on Coding:

Implement Prim’s and Kruskal’s

Track parent arrays and sets

Solve 1–2 MST problems

Day 5: Advanced Graph Problem Solving Patterns

Topics:

Graph patterns:

Topological sorting (DAGs)

Detect cycles in directed/undirected graphs

Strongly connected components (Kosaraju’s / Tarjan’s)

Recognize which traversal and algorithm to apply

Dependencies: BFS/DFS (Week 7), weighted graph algorithms (Days 1–4)

Code Folder: Code/python/week-08/day-05-graph-problems-advanced/
Documentation Link: 04-Advanced-DSA/graphs/cycle-detection.md

Hands-on Coding:

Solve 3–5 advanced graph problems

Annotate patterns, time/space complexities

Add post-mortem notes for mistakes and optimization ideas

Daily Execution Rules (Non-Negotiable)

90 minutes per day dedicated to learning + coding

Follow concept → pattern → code → optimization → documentation

Revise previous topics 5–10 minutes/day (Week 7 + Week 6 trees)

Commit code + notes at the end of each day

Maintain links to weekly MD file + documentation for easy navigation

✅ Outcome of Week 8:

Solid understanding of weighted graphs, shortest path, MSTs

Able to implement Dijkstra, Bellman-Ford, Prim’s & Kruskal’s algorithms

Recognize graph problem patterns for FAANG-level problems

Coding exercises fully linked with documentation
