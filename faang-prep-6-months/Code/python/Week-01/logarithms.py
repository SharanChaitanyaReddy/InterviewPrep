# Experiment 1: Binary Search Iterations

# Write a function that performs binary search on a sorted list of length n.

# Count how many comparisons it makes.

# Check for n = 8, 16, 32.

# Observe the number of iterations vs input size.

def binary_search(arr, target):
    print("Array:", arr)
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        count += 1
        if arr[mid] == target:
            print("Mid index:", mid)
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print("Total iterartions after halving:", count)
#[1,2,3,4,5]


binary_search(list(range(8)), 7)  # n = 8
binary_search(list(range(16)), 4)  # n = 16
binary_search(list(range(16)), -1)  # n = 16 
binary_search(list(range(32)), 31)  # n = 32 
binary_search(list(range(32)), -1)  # n = 32 


binary_search(list(range(8)), 4)  # n = 8
binary_search(list(range(16)), 4)  # n = 16
binary_search(list(range(32)), 4)  # n = 32

n = 32
i = n
count = 0
while i > 0:
    i //= 2
    # print("i:", i)
    count += 1
print("Iterations:", count)



# Experiment 3: Recursive Halving

# Implement a recursive function that prints n and calls itself with n//2.

def recursive_halve(n):
    if n == 0:
        return
    print("n:", n)
    recursive_halve(n // 2)


recursive_halve(8)
