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

# Experiment 3: Immutable Change
print("---Experiment 3: ---")
d = 10
e = 10
e += 5
d += 5
print(d, e)
print(id(d), id(e))


#Experiment 4: Mutable Objects
print("---Experiment 4: Mutable Objects---")
m = [1, 2, 3]
n = m

m.append(4)

print(m, n)
print(id(m), id(n))

#Experiment 4: Copying Lists
k = [1, 2]
m = k
n = k[:]

k.append(3)

print(k)
print(m)
print(n)