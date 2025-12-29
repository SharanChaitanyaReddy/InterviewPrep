Input / Output & Type Conversion (Python)
A. Why this matters (Interview + Real World)


Most bugs in early rounds come from wrong input type assumptions


Many performance bugs come from unnecessary conversions


Python is dynamically typed, but not magically typed



B. Input in Python (What REALLY happens)
x = input("Enter a number: ")
print(x, type(x))

🧠 Key fact (non-negotiable):

input() ALWAYS returns a string

Even if the user types:
10

Python sees:
"10"   # string


C. Type Conversion (Explicit is mandatory)
x = input("Enter a number: ")
y = int(x)

print(y, type(y))

Now:


"10" → 10


string → integer



D. Common Conversions You MUST Know
ConversionExampleNotesstr → intint("10")fails on "10.5"str → floatfloat("10.5")safe for decimalsint → strstr(10)used in printingfloat → intint(10.9)truncates, not roundsbool → intint(True) → 1interview favorite

E. Dangerous Conversions (Interview Traps)
❌ This crashes
int("10.5")

❌ This crashes
int("abc")

❌ Silent bug
print("10" + "20")   # "1020"
print(10 + 20)       # 30


F. Output Formatting (Real-world important)
Old style (don’t use)
print("Value is %d" % x)

Better
print("Value is", x)

Best (modern Python)
print(f"Value is {x}")

Why f-strings?


Faster


Cleaner


Less error-prone



G. Performance Note (Important for FAANG)


Type conversion inside loops is expensive


Convert once, use many times


❌ Bad:
for _ in range(1000000):
    x = int(input_value)

✅ Good:
x = int(input_value)
for _ in range(1000000):
    use(x)


🧪 Experiment for YOU (Answer before we move on)
Experiment 1
a = input("Enter: ")
b = a + "1"
print(b)

❓ Question:
If user enters 5, what is printed and why?
Output = 51
Since input provided is always string + in a +"1" wikl  concat the strings.

Experiment 2
a = int(input("Enter: "))
b = a + 1
print(b)

❓ Question:
What changed compared to Experiment 1?

The input string is converted to int before assigning to variable a.

Experiment 3 (Trick)
print(bool("False"))

❓ Question:
What does this print and why?
This prints True because it checks the string empty or has values and returns true/false.
