#Experiment 1: Variable References
print("---Experiment 1: Variable References---")
a = 10
b = a

print(a,b)

print(id(a), id(b))



# Experiment 2: Immutable Change
print("---Experiment 2: Immutable Change---")
x = 10
y = x
x = 20

print(x, y)
print(id(x), id(y))



#Experiment 3: Mutable Objects
print("---Experiment 3: Mutable Objects---")
m = [1, 2, 3]
n = m

m.append(4)

print(m, n)
print(id(m), id(n))