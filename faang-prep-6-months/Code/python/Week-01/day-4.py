

def multiply(n):
    i = 1
    count = 0
    while i < n:
        i = i *2
        count += 1
    print(f"Total iterations in multiplication for {n}: {count} and {i}")

multiply(8)



#------------------------------

 #Write a loop that:
# Iterates beyond array length

# Uses modulo to stay in bounds

arr = [1, 2, 3, 4, 5]
i = 0
array_length = len(arr)
while i < 10:
    #print(f"len(arr) : {array_length} and i: {i}")
    print(arr[i % array_length])
    i += 1


# Experiment 2: Circular Movement

# Simulate moving forward and backward on a circular list.

print("Circular Movement")
forward = True
i = 0
countThis = 0
while i < 10:
    if countThis >= 10:
        break
    print(arr[i % array_length])
    countThis += 1
    i += 1
    if i == array_length:
        forward = False
    elif i == -1:
        forward = True
    i += 1 if forward else -1


print("------------Circular Movement-------------------")
circularArr = [1,2,3,4,5]
i = 0
backward = False
count = 0
while i < 15:
    if count >= 15:
        break
    print(circularArr[i % len(circularArr)])
    count += 1
    if not backward:
        i += 1
    else:
        i -= 1
    if i == 0:
        backward = False
    if i >= len(circularArr):
        backward = True


print("------------Circular Movement Optimized-------------------")
circularArr_ = [1, 2, 3, 4, 5]

j = 0
direction = 1   # +1 = forward, -1 = backward
steps = 15
n = len(circularArr_)

for _ in range(steps):
    print(circularArr_[j])

    # Reverse direction BEFORE hitting boundary
    if j == 0:
        direction = 1
    elif j == n - 1:
        direction = -1

    j += direction



# Experiment 3: Hash Bucket Simulation

# Create:

# A fixed-size list (buckets)

# Insert values using value % size


fixed_list = [None] * 10
k = 0
while k < 15:
    index = k % len(fixed_list)
    print(f"Inserting {k} into bucket {index}")
    fixed_list[index] = k
    k += 1
print(f"Hash Bucket Simulation Result: {fixed_list}")

# Experiment 4: Large Number Control

# Compute:

# A very large multiplication

# Compare results with and without modulo

large_number = 10000000000 * 10000000000
print(f"Large Multiplication Result (with modulo): {large_number % 100}")
print(f"Large Multiplication Result (without modulo): {large_number}")
