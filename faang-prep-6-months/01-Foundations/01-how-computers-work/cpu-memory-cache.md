Week 1 – Day 2
How Computers Actually Work (For Programmers)

Goal of Day 2
Not to memorize theory — but to build an internal mental model of what happens under the hood when you write Python.

If this mental model is weak, DSA feels fake and confusing later.

⏱️ Time Split (90 minutes)

20 min → Concept reading + thinking

40 min → Hands-on experiments (you do them)

20 min → Answer questions (in your own words)

10 min → Notes + checklist update

1️⃣ Core Concepts (You Must Understand These)
A. What a Computer Really Is

At its core, a computer has:

CPU → executes instructions

Memory (RAM) → stores data temporarily

Storage (Disk) → stores data permanently

💡 Python is not running magically — it’s just CPU instructions + memory changes.

B. What Happens When You Run a Python File

When you run:

python test.py


Internally:

OS loads Python interpreter into memory

Interpreter reads your file top to bottom

Each line is:

Parsed

Converted to bytecode

Executed by the Python Virtual Machine (PVM)

Variables → stored in memory

Program ends → memory is released

👉 Python is interpreted, not compiled (for our purposes).

C. Memory Basics (Very Important)

When you write:

x = 10


What actually happens:

10 is stored somewhere in memory

x is a label pointing to that memory

Python variables are references, not boxes.

This single idea explains:

Mutability

Bugs

Performance

Interview trick questions

2️⃣ Hands-On (DO THIS — No Skipping)

Create a file:

Experiment 1: Variable References
a = 10
b = a

print(a, b)
print(id(a), id(b))


✍️ You must answer:

Why are id(a) and id(b) the same?

Did Python copy the value or the reference?

What Happened:

a = 10

Python creates an integer object 10 in memory.

a becomes a reference (pointer) to that object.

b = a

b is now assigned the same reference as a.

Both a and b point to the same object in memory, they do not create a new copy.

print(a, b)

Both print 10 because both a and b refer to the same object.

print(id(a), id(b))

id() shows the memory location of the object.

Both IDs are identical → confirms same object is referenced by both a and b.

✅ Corrected  Explanation:

When you assign b = a, Python does not copy the value. Instead, b points to the same object in memory as a.
Both a and b reference the integer 10. That’s why printing id(a) and id(b) gives the same memory location.
This illustrates that Python variables are references, not boxes containing values.

Key Takeaways:

Assignment copies references, not values.

Immutable objects (like integers, strings, tuples) mean changing one variable creates a new object.

This understanding is critical to avoid confusion with mutables, which we’ll see in Experiment 3.


Experiment 2: Immutable Change
a = 10
b = a
a = 20

print(a, b)
print(id(a), id(b))


✍️ Answer:

Why didn’t b change?

What changed in memory?

1. Why didn’t b change?

When b = a is executed, both a and b point to the same object 10.

Later, a = 20 reassigns a to a new object 20.

b still points to the original object 10.

Assignment does not “back-propagate” to other references.

Step 1: a = 10
Memory: [10]
a ---> [10]

Step 2: b = a
Memory: [10]
a ---> [10]
b ---> [10]

Step 3: a = 20
Memory: [10], [20]
a ---> [20]  # new object
b ---> [10]  # unchanged

2. What changed in memory?

A new integer object 20 is created.

a now references this new object.

The old object 10 still exists in memory (referenced by b).

This behavior happens because integers are immutable. Reassigning creates a new object instead of modifying the existing one.


Experiment 3: Mutable Objects
x = [1, 2, 3]
y = x

x.append(4)

print(x, y)
print(id(x), id(y))


✍️ Answer:

Why did both change?

Why is this dangerous in interviews?

1. Why did both x and y change?

Lists are mutable objects in Python.

When y = x is executed, both x and y reference the same list object in memory.

Modifying the list using x.append(4) changes the object in-place.

Since y points to the same object, it also reflects the change.

Memory diagram:
x ---> [1, 2, 3]
y ---/
After x.append(4):
x ---> [1, 2, 3, 4]
y ---/

2. Why is this important / dangerous in interviews?

If you accidentally mutate a shared object, it can lead to unexpected side-effects in your code.

This is especially tricky in functions or class attributes where multiple references point to the same mutable object.

Interviewers may ask about copy vs reference behavior to test your understanding of mutability.

✅ Documentation Note:

Mutable objects like lists, dictionaries, and sets can be changed in-place. Assigning one variable to another does not create a copy; both variables point to the same object. Always be cautious when mutating objects that have multiple references.

3️⃣ CPU Thinking (Interview-Level Skill)

Think like the CPU:

CPU does one instruction at a time

No “jumping”

No “understanding intent”

Example:

x = x + 1


This is actually:

Load x

Load 1

Add

Store result

Update reference

💡 This matters for:

Loops

Time complexity

Optimization

4️⃣ You Answer These (Mandatory)

Write answers in your own words (not here — in your repo notes):

What is the difference between RAM and Disk?
RAM is temporary memory
Disk is permanent storage

What does the Python interpreter do?
Reads the Python Code line by line and parses it

Takes your .py file (or interactive input) and reads it line by line.

Checks for syntax errors. If there are mistakes, it stops and reports them.

Example:

print("Hello World")


The interpreter first checks if this is a valid Python statement.

2. Compiles to Bytecode

Python is an interpreted language, but internally, the interpreter compiles your code to bytecode.

Bytecode is a low-level, platform-independent representation of your code.

This bytecode is stored in .pyc files (inside __pycache__) for faster execution next time.

3. Executes Bytecode

The interpreter sends the bytecode to the Python Virtual Machine (PVM).

The PVM executes instructions line by line, interacting with memory, variables, objects, and performing operations.

4. Manages Memory and Objects

Keeps track of variables and objects.

Handles mutable vs immutable objects, reference counting, and garbage collection.

5. Handles Errors at Runtime

If an operation fails (like dividing by zero), the interpreter raises a runtime error.

Example:

x = 10 / 0  # Raises ZeroDivisionError

✅ Key Points

Python interpreter = reads → compiles → executes your code.

It abstracts away memory management and low-level operations, so you focus on writing logic.

Explains why mutable vs immutable behavior and variable references matter — the interpreter manages object references and memory behind the scenes.


What does id() represent?
id() shows the memory location of the object.

Why are Python variables called references?
Variables in  py refer to objects in memeory they don't directly store the values.

Why are mutable objects risky?
Mutable objects like lists, dictionaries, and sets can be changed in-place. Assigning one variable to another does not create a copy; both variables point to the same object. Always be cautious when mutating objects that have multiple references.

If you can’t answer cleanly → re-read and re-test.

5️⃣ Mini Challenge (Think, Don’t Run First)

Before running this, predict output:

a = [1, 2]
b = a
c = a[:]

a.append(3)

print(a)
print(b)
print(c)


✍️ Write your prediction → THEN run → explain mismatch (if any).

This prediction habit is critical for FAANG interviews.

a = [1, 2] → Creates a list object [1, 2] in memory.

b = a → b references the same list object as a.

c = a[:] → This creates a shallow copy of the list [1, 2]. c points to a different object in memory, but initially contains the same elements.

Memory diagram:

a ---> [1, 2]
b ---^
c ---> [1, 2]   (different object)

Step 2: Append operation
a.append(3)


a now becomes [1, 2, 3].

b points to the same object, so it also sees [1, 2, 3].

c is a copy, so it remains [1, 2].

Step 3: Print statements
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]  (same object as a)
print(c)  # [1, 2]     (different object)

✅ Key Takeaways:

Assignment copies references, not the object itself: b = a → both refer to the same list.

Shallow copy (a[:]) creates a new object but does not deep-copy nested objects.

Modifying a mutable object affects all variables referencing it, except copies.


6️⃣ What NOT To Do Today ❌

No LeetCode

No YouTube

No frameworks

No optimization obsession

Today is about mental clarity, not speed.

7️⃣ End-of-Day Checklist (Tick These)

 Ran all experiments

 Wrote answers in my own words

 Can explain references vs values without code

 Committed files + notes

 Updated Week 1 tracker

Calm Motivation (Not Cringe)

“Clarity before speed. Depth before volume.”

You are building foundations, not chasing dopamine.

Next (Only After You Finish This)

👉 Day 3: Practical Math for Programmers (Counting & Growth)
This is where DSA actually begins.

When you’re done with Day 2, don’t say “done”.
Say:

“I can explain this without code.”

That’s the standard now.