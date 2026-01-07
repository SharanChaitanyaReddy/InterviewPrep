🔁 Core Programming & CS Recap (Mental Model First)

Goal:
When solving a problem, this recap should automatically surface the right idea.

1️⃣ Variables, Objects & References (Python Mental Model)
Think this when:

Assigning variables

Passing values to functions

Seeing unexpected changes

Core Truth

Variables do not store values

Variables reference objects in memory

Immutable vs Mutable

Immutable: int, float, str, tuple

Mutable: list, dict, set

Trigger Pattern

“Did this variable change itself, or did it point to a new object?”

Snippet
a = 10
b = a
a = 20
# b is still 10 → new object created

x = [1, 2]
y = x
x.append(3)
# y also changes → same object

2️⃣ Copying vs Sharing Objects
Think this when:

You don’t want side effects

Passing lists into functions

Rule

= → same object

[:] or .copy() → new object

Snippet
a = [1, 2]
b = a
c = a[:]

a.append(3)
# b changes, c does not

3️⃣ Input, Types & Truthiness
Think this when:

Using input()

Checking conditions

Core Rules

input() → always string

Non-empty strings → True

Snippet
bool("False")  # True
bool("")       # False

4️⃣ Stack vs Heap (Mental Model Only)
Think this when:

Recursion

Function calls

Performance discussions

Stack

Function calls

Local variables

LIFO

Limited size

Heap

Objects

Lists, dicts

Managed by Python

Snippet
def f():
    x = 10  # reference on stack → object on heap

5️⃣ Counting = Performance Intuition
Think this when:

Estimating time complexity

Comparing approaches

Rule

Count operations, not lines of code

Patterns

Separate loops → add

Nested loops → multiply

Snippet
for i in range(n): pass
for j in range(n): pass
# ~2n

for i in range(n):
    for j in range(n):
        pass
# ~n²

6️⃣ Growth Patterns (MOST IMPORTANT)
Always ask:

“How does work grow when input grows?”

Cheat Sheet
Pattern	Meaning
O(1)	Constant
O(n)	Linear
O(n²)	Quadratic
O(log n)	Halving
O(2ⁿ)	Exponential
7️⃣ Exponential vs Logarithmic (Opposites)
Exponential

Repeated work

Recursive branching

No memoization

def fib(n):
    return fib(n-1) + fib(n-2)

Logarithmic

Halving input

Binary search

Divide & conquer

while n > 1:
    n //= 2

8️⃣ Binary Search Thinking
Think this when:

Sorted data

“Find” or “search”

Large input

Core Idea

Each step removes half the work

Snippet
while low <= high:
    mid = (low + high) // 2

Mental Check

Doubling input → +1 step

That’s why it’s fast

9️⃣ Modulo (%) = Cycles & Control
Think this when:

Circular movement

Hashing

Repeating patterns

Core Rule
index = i % size

Snippet
arr = [1,2,3]
arr[5 % 3]  # arr[2]

Python Special
-1 % 5 == 4

🔟 Modulo → Hashing → Collisions → Chaining
Mental Flow

Modulo maps large numbers → small buckets

Multiple values can map to same bucket

Collision happens

Chaining stores multiple values

Snippet
bucket = value % bucket_count

Key Insight

Modulo controls range

It does not eliminate collisions

1️⃣1️⃣ Cache & Memory Access (Performance Layer)
Think this when:

Nested loops

2D arrays

Performance tuning

Rule

Contiguous memory = faster

Pattern

Row-wise access → cache-friendly

Column-wise access → cache misses

1️⃣2️⃣ Function Calls vs Simple Operations
Think this when:

Micro-optimizations

Tight loops

Truth

Function calls are expensive

You proved this ✔

Stack frame creation

Parameter passing

Return handling

🧠 Final Mental Checklist (Run This While Solving Problems)

Ask yourself:

Is this mutable or immutable?

Am I sharing or copying?

How does work grow with input?

Is this repeated work?

Can I halve the input?

Is modulo hiding a cycle?

Could memory access be slow?


