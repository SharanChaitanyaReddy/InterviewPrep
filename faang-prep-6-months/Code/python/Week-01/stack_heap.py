#Experiment 1
def foo():
    x = 10
    return x

print(foo())

#Experiment 2
def a():
    b()

def b():
    c()

def c():
    print("Hello")

a()

#Experiment 3
def recurse():
    print("Recursing...")
#    recurse() #(Uncomment this line to see the recursion in action)

recurse()

#Experiment 4
def add_item(lst):
    lst.append(4)

x = [1, 2, 3]
add_item(x)
print(x)