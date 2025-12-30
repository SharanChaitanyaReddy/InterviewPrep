Topic: Stack vs Heap Memory (Python-centric, Interview-grade)

This topic answers why recursion fails, why programs slow down, and why Python behaves “magically” sometimes.

1️⃣ High-Level Mental Model (No Jargon First)

Think of memory like this:

🧱 Stack

Fast

Limited size

Stores function calls, local variables, references

Grows & shrinks automatically

🏗️ Heap

Large

Slower than stack

Stores objects (lists, dicts, ints, strings, class instances)

Managed by Python (garbage collection)

📌 Important:
Python variables do not store values, they store references to heap objects.

2️⃣ What Goes Where in Python?

Let’s test your intuition.

Experiment 1
def foo():
    x = 10
    return x

foo()


❓ Question :

Is x on stack or heap?

Is 10 on stack or heap?

👉 Answer (after you think):

x → stack (reference)

10 → heap (integer object)

3️⃣ Stack in Action (Function Calls)
Experiment 2
def a():
    b()

def b():
    c()

def c():
    print("Hello")

a()


📌 What happens internally:

Stack:
a()
  b()
    c()


Each function call:

Pushes a stack frame

Contains local variables + references

Pops when function returns

4️⃣ Recursion = Stack Growth (Danger Zone)
Experiment 3
def recurse():
    recurse()

recurse()


❓ Question:
Why does this crash?

👉 Correct Explanation:

Each recursive call creates a new stack frame

Stack memory is finite

Python raises RecursionError to prevent stack overflow
(RecursionError: maximum recursion depth exceeded)
📌 Python default recursion limit ≈ 1000

5️⃣ Heap in Action (Mutable Objects)
Experiment 4
def add_item(lst):
    lst.append(4)

x = [1, 2, 3]
add_item(x)
print(x)


❓ Question:
Why does x change even though it wasn’t returned?

👉 Key Insight:

x (stack) points to a list object in heap

lst points to the same object

Mutation affects the shared object

6️⃣ Stack vs Heap Summary (Interview Gold)
Concept	Stack	Heap
Speed	Very fast	Slower
Size	Limited	Large
Stores	Function frames, references	Objects
Lifetime	Automatic	Garbage collected
Risk	Stack overflow	Memory leaks (long-lived refs)
7️⃣ 🔥 Interview Trap Question

❓ Why are recursive Python programs slower than iterative ones?

💡 Strong Answer:

Recursive calls add stack frames, function call overhead, and risk hitting recursion limits. Iterative solutions reuse a single frame and are more memory-efficient.

8️⃣ Your Turn 

Answer in your own words:

Why do mutable objects cause bugs in functions?
 If Mutable objects are refered from more than one vriable and one updates the object other will also be effected this creats uncertainity

 (Mutable objects cause bugs because multiple variables can reference the same object in memory. When one reference mutates the object, the change is visible to all references, often leading to unintended side effects across functions.)

Why doesn’t Python store values directly on the stack?

(Python does not store values directly on the stack because:

Stack size is limited

Objects in Python are:

Dynamic in size

Can outlive function calls

Can be shared across functions

Python uses reference semantics for flexibility and safety)

What happens in memory when a recursive function returns?
gets poped and memory is freed

(When a recursive function returns, its stack frame is popped, removing local references. Heap objects remain in memory until no references exist, after which Python’s garbage collector may reclaim them.

📌 Important distinction:
Stack cleanup ≠ Heap cleanup)
