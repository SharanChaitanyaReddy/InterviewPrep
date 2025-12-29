2️⃣ Operators & Expressions

Python provides several types of operators to perform operations on variables and values:

1. Arithmetic Operators
Operator	Meaning	Example	Output
+	Addition	3 + 2	5
-	Subtraction	5 - 3	2
*	Multiplication	4 * 2	8
/	Division (float)	5 / 2	2.5
//	Floor Division	5 // 2	2
%	Modulus (remainder)	5 % 2	1
**	Exponentiation	2 ** 3	8

💡 Tip: / always returns float, // returns integer (floor division).

2. Comparison Operators
Operator	Meaning	Example	Output
==	Equal	5 == 5	True
!=	Not Equal	5 != 3	True
>	Greater than	5 > 3	True
<	Less than	3 < 5	True
>=	Greater Equal	5 >= 5	True
<=	Less Equal	3 <= 5	True

3. Logical Operators
Operator	Meaning	Example	Output
and	Logical AND	True and False	False
or	Logical OR	True or False	True
not	Logical NOT	not True	False

4. Assignment Operators
Operator	Meaning	Example
=	Assign	a = 10
+=	Add & assign	a += 2 → a = a+2
-=	Subtract & assign	a -= 3 → a = a-3
*=	Multiply & assign	a *= 4
/=	Divide & assign	a /= 2

5. Identity Operators
Operator	Meaning	Example
is	True if same object	a is b
is not	True if not same object	a is not b

💡 Tip: is checks if two variables point to same object in memory, not just equal values.

Mini Experiment for You

Try this:

# Arithmetic
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Logical
x = True
y = False
print(x and y, x or y, not x)

# Identity
m = [1,2,3]
n = m
o = [1,2,3]
print(m is n)   # True or False?
print(m is o)   # True or False?


✅ Questions to answer yourself:

What is the difference between / and //?

Why m is n is True but m is o is False?

How would you use += or -= in a loop efficiently?

1️⃣ Difference between / and //

/ → True division (always returns a float)

5 / 2  # 2.5


Even if both operands are integers, the result is a float.

// → Floor division (returns the largest integer ≤ division result)

5 // 2  # 2


Floor division truncates the decimal part and returns an integer (or float if one operand is float).

💡 Tip: Use / when you need exact division, use // when you want integer results or indexes.

2️⃣ Why m is n is True but m is o is False?
m = [1,2,3]
n = m
o = [1,2,3]

m is n  # True
m is o  # False


is checks identity, i.e., whether two variables point to the same object in memory.

n = m → n points to the same object as m. ✅

o = [1,2,3] → creates a new object in memory, even though the values are the same. ❌

So m is o is False, but m == o (value comparison) would be True.

💡 Tip: Mutable objects like lists or dicts can cause confusion if you accidentally modify one reference, it affects the other.

3️⃣ How to use += or -= efficiently in a loop

+= and -= are shorthand assignment operators, which combine operation + assignment.

Example: summing numbers

total = 0
for i in range(1, 6):
    total += i  # equivalent to total = total + i
print(total)  # 15


Similarly, decrementing

x = 10
for _ in range(5):
    x -= 1  # subtract 1 in each iteration
print(x)  # 5


✅ Advantages:

Cleaner code

Slightly more efficient than writing x = x + y repeatedly

Helps in counters, sums, accumulation patterns
