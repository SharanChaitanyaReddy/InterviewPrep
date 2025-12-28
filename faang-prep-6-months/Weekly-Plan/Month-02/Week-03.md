# Week 7 – Month 2: Graphs – Basics & Traversals

**Objective:**  
Understand graph data structures, node relationships, traversal patterns (BFS, DFS), and applications. Build on tree knowledge (Week 6) and recursion (Week 5).

---

## Folder Structure for Code

```
Code/python/week-07/
├── day-01-graph-intro/
├── day-02-adjacency-representation/
├── day-03-bfs-traversal/
├── day-04-dfs-traversal/
└── day-05-graph-problems/
```

---

## Day 1: Graph – Introduction

**Topics:**
- What is a graph? Nodes (vertices) and edges
- Types of graphs: Directed, Undirected, Weighted, Unweighted
- Real-world analogy: Social networks, road maps, dependency graphs
- When to use graphs vs trees/arrays

**Dependencies:** Trees (Week 6), recursion (Week 5)  
**Code Folder:** `Code/python/week-07/day-01-graph-intro/`  
**Documentation Link:** `04-Advanced-DSA/graphs/bfs-dfs.md`  

**Hands-on Coding:**
- Create a simple graph class in Python
- Add vertices and edges manually
- Print adjacency list representation

---

## Day 2: Graph Representations

**Topics:**
- Adjacency list vs adjacency matrix
- Edge list representation
- Time/space complexity trade-offs
- Choosing representation for BFS/DFS

**Dependencies:** Day 1 graph intro, Python lists/dicts (Week 2)  
**Code Folder:** `Code/python/week-07/day-02-adjacency-representation/`  
**Documentation Link:** `04-Advanced-DSA/graphs/bfs-dfs.md`  

**Hands-on Coding:**
- Implement adjacency list and matrix
- Write helper functions: add edge, remove edge, display graph
- Compare memory usage between representations

---

## Day 3: BFS – Breadth-First Search

**Topics:**
- BFS algorithm and queue usage
- Level-order traversal analogy from trees
- Shortest path in unweighted graph
- BFS template for coding problems

**Dependencies:** Day 2 adjacency representation, queues/stacks (Week 3)  
**Code Folder:** `Code/python/week-07/day-03-bfs-traversal/`  
**Documentation Link:** `04-Advanced-DSA/graphs/bfs-dfs.md`  

**Hands-on Coding:**
- BFS traversal of a graph
- Track visited nodes
- Solve 1–2 BFS practice problems
- Annotate time/space complexity

---

## Day 4: DFS – Depth-First Search

**Topics:**
- DFS algorithm and recursion usage
- DFS iterative using stack
- Connected components detection
- Cycle detection intro

**Dependencies:** Day 2 adjacency representation, recursion (Week 5)  
**Code Folder:** `Code/python/week-07/day-04-dfs-traversal/`  
**Documentation Link:** `04-Advanced-DSA/graphs/bfs-dfs.md`  

**Hands-on Coding:**
- DFS traversal (recursive and iterative)
- Detect connected components in a graph
- Annotate recursive calls and stack usage

---

## Day 5: Graph Problem Solving Patterns

**Topics:**
- Graph problem patterns:
  - Shortest path (unweighted)
  - Detect cycle
  - Connected components
- Recognize which traversal to use when
- Applying BFS/DFS templates

**Dependencies:** BFS (Day 3), DFS (Day 4)  
**Code Folder:** `Code/python/week-07/day-05-graph-problems/`  
**Documentation Link:** `04-Advanced-DSA/graphs/shortest-path.md`  

**Hands-on Coding:**
- Solve 3–5 graph problems
- Annotate base case, recursion depth, queue/stack usage
- Time/space complexity notes
- Prepare notes linking to upcoming Weighted Graphs & Dijkstra

---

## Daily Execution Rules (Non-Negotiable)

- 90 minutes per day dedicated to learning + coding
- Follow concept → pattern → code → optimization → documentation
- Revise previous topics 5–10 minutes/day (trees, recursion)
- Commit code + notes at the end of each day
- Maintain links to weekly MD file + documentation for easy navigation

---

## ✅ Outcome of Week 7

- Solid understanding of basic graphs and traversals
- BFS & DFS fully implemented with coding exercises
- Linked coding exercises with GitHub folder
- Dependencies maintained for Week 8 (Weighted Graphs & Advanced Graph Problems)
