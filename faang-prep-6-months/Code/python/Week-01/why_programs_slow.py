#Experiment 1: String vs List Concatenation
# Inefficient
s = ""
for l in range(1000):
    s += str(l)

# Efficient
lst = []
for l in range(1000):
    lst.append(str(l))
s2 = "".join(lst)


#Experiment 2: List vs Set Membership
import timeit

# Using timeit in a script
my_list = list(range(1000000))
my_set = set(range(1000000))

# List membership check
time_list = timeit.timeit("999 in my_list", globals=globals(), number=1000)
print(f"List check: {time_list:.6f} seconds")

# Set membership check
time_set = timeit.timeit("999 in my_set", globals=globals(), number=1000)
print(f"Set check: {time_set:.6f} seconds")


#Experiment 3: Loop Optimization
# Slow
new_list = [1, 2, 3, 4, 5]
for g in range(len(new_list)):
    print(new_list[g])

# Fast (Pythonic)
for item in new_list:
    print(item)


#Experiment 4: Cache-friendly Access
matrix = [[i+j for j in range(1000)] for i in range(1000)]

# Row-wise (fast)
for row in matrix:
    for val in row:
        pass

# Column-wise (slow)
for j in range(1000):
    for i in range(1000):
        val = matrix[i][j]



#Experiment 5
matrix = [[a+b for b in range(1000)] for a in range(1000)]

# Row-wise iteration (fast)
import time
start = time.time()
for row in matrix:
    for val in row:
        pass
print("Row-wise:", time.time() - start)

# Column-wise iteration (slow)
start = time.time()
for j in range(1000):
    for i in range(1000):
        val = matrix[i][j]
print("Column-wise:", time.time() - start)


import numpy as np
matrix_np = np.arange(1000*1000).reshape(1000,1000)

# Define a function that iterates in row-major order
def row_major_access():
    for i in range(1000):
        for j in range(1000):
            _ = matrix_np[i, j]

# Define a function that iterates in column-major order
def column_major_access():
    for j in range(1000):
        for i in range(1000):
            _ = matrix_np[i, j]

# Measure execution time
execution_time = timeit.timeit(row_major_access, number=1)
print("Row-major access time:", execution_time)

execution_time = timeit.timeit(column_major_access, number=1)
print("Column-major access time:", execution_time)