# Month 04 - Week 02 Plan – FAANG Prep

## 1. Motivation & Focus Reminder
- This 90-minute daily preparation is **non-negotiable**.
- Remember why you are doing this: building skills for **FAANG / top MNC**, mastering **DSA**, **system design**, and **AI fundamentals**.
- Focus on **small wins every day**, not the entire roadmap at once.
- Keep distractions away: phone on silent, no YouTube rabbit holes.

---

Week 14 – Month 4: Advanced Graph Problems & Graph DP

Objective:

Solve advanced graph problems like topological sort, strongly connected components (SCC), and graph dynamic programming

Connect graph DP to problem-solving patterns

Folder structure for code:

Code/python/week-14/
├── day-01-topological-sort/
├── day-02-kahns-algorithm/
├── day-03-scc-kosaraju-tarjan/
├── day-04-graph-dp-intro/
├── day-05-graph-dp-problems/
└── day-06-week-review-postmortem/

Day 1: Topological Sort

Topics:

Concept of topological ordering in DAG (Directed Acyclic Graph)

Real-world use cases: task scheduling, course prerequisites

Recursive & iterative implementation

Dependencies:

BFS/DFS (Week 13)

Graph representation (adjacency list)

Code Folder: Code/python/week-14/day-01-topological-sort/
Documentation Link: 04-Advanced-DSA/graphs/topological-sort.md

Hands-on Coding:

Implement DFS-based topological sort

Solve small DAG problems

Day 2: Kahn’s Algorithm (BFS for Topological Sort)

Topics:

Queue-based approach for topological sorting

Compare DFS vs Kahn’s algorithm

Detect cycles in DAG

Dependencies:

Day 1 (Topological Sort)

Queues, graph traversal

Code Folder: Code/python/week-14/day-02-kahns-algorithm/
Documentation Link: 04-Advanced-DSA/graphs/topological-sort.md

Hands-on Coding:

Implement Kahn’s algorithm

Solve DAG problems with edge cases & cycle detection

Day 3: Strongly Connected Components (SCC)

Topics:

Concept of SCC in directed graphs

Kosaraju’s algorithm (two DFS passes)

Tarjan’s algorithm (single DFS + lowlink values)

Applications: network analysis, dependency detection

Dependencies:

DFS (Week 13), topological sort (Days 1–2)

Stack usage

Code Folder: Code/python/week-14/day-03-scc-kosaraju-tarjan/
Documentation Link: 04-Advanced-DSA/graphs/scc.md

Hands-on Coding:

Implement Kosaraju & Tarjan algorithms

Annotate why each step is needed and complexity

Day 4: Graph Dynamic Programming – Introduction

Topics:

Concept of graph DP

When to apply DP on DAGs

Examples: longest path in DAG, counting paths

Dependencies:

Topological sort, DAG knowledge (Days 1–2)

DP concepts (Weeks 10–12)

Code Folder: Code/python/week-14/day-04-graph-dp-intro/
Documentation Link: 04-Advanced-DSA/graphs/graph-dp.md

Hands-on Coding:

Solve longest path in DAG using DP

Annotate recurrence relation & dependencies

Day 5: Graph DP Problems

Topics:

Counting paths in DAG

Minimum/maximum cost paths

Real-world examples: project planning, network flow prep

Dependencies:

Day 4 (graph DP intro)

DP memoization & tabulation

Code Folder: Code/python/week-14/day-05-graph-dp-problems/
Documentation Link: 04-Advanced-DSA/graphs/graph-dp.md

Hands-on Coding:

Solve 1–2 medium graph DP problems

Annotate edge cases & complexity analysis

Day 6: Week Review & Postmortem

Topics:

Consolidate advanced graph concepts & DP problems

Timed coding practice for topological sort, SCC, graph DP

Identify weak areas & dependencies for revision

Dependencies:

Days 1–5 (all advanced graph topics)

Code Folder: Code/python/week-14/day-06-week-review-postmortem/
Documentation Link: Revision/weekly-review.md

Hands-on Coding:

Solve 1–2 mixed graph problems in timed session

Maintain postmortem notes linking to weekly MD file

Daily Execution Rules (Non-Negotiable)

90 minutes/day minimum

Concept → Pattern → Code → Optimization → Documentation

Revise previous weeks 5–10 minutes/day

Commit code + notes end of each day

Maintain links to weekly MD + documentation

✅ Outcome of Week 14:

Master topological sort, SCC, and graph DP

Hands-on coding & timed problem-solving

Clear linkage between code → weekly MD → revision notes

Ready to move on to Mixed Graph & Advanced DP Problems in Week 15
