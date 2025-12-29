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


#Example: summing numbers

total = 0
for i in range(1, 6):
    total += i  # equivalent to total = total + i
print(total)  # 15


#Similarly, decrementing

k = 10
for _ in range(5):
    k -= 1  # subtract 1 in each iteration
print(k)  # 5