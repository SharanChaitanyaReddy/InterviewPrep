#Write a loop that prints numbers from 1 to n

#Count how many print operations happen

#Change n from 10 → 1,000 → 1,000,000

#Write down the pattern you observe

def counting_growth(n):
    count = 0
    for i in range(1,n +1):
        #print(i)
        count += 1
    print("Total print operations:", count)

counting_growth(10)
# counting_growth(1000)
# counting_growth(1000000)


#Write two versions:

#One loop

#Two nested loops
#Without naming Big-O, count total operations

def count_operations(n):
    # One loop
    count = 0
    for i in range(1, n + 1):
        count += 1
    print("Total operations (one loop):", count)

    # Two nested loops
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count += 1
    print("Total operations (two nested loops):", count)

count_operations(10)
# count_operations(1000)
# count_operations(10000)


#Modify the nested loop so the inner loop runs only half as many times

#Does the count change linearly or quadratically?

def counting_operation_modified(n):
    # Two nested loops with inner loop running half as many times
    count = 0
    for i in range(1, n + 1):
        for j in range(1, (n // 2) + 1):
            count += 1
    print("Total operations (nested loops with half inner):", count)

counting_operation_modified(10)
# counting_operation_modified(1000)
# counting_operation_modified(10000)

#(Sequential vs Nested Work)


#Create two loops that run one after another

#Count total iterations

#Create one loop inside another

#Count total iterations

#Increase input size:

#Double n

#What happens to the total count in each case?

#Write the growth relationship in words, not symbols.

def two_loops_run_one_after_another(n):
    count = 0
    count_loop1 = 0
    for i in range(1, n+1):
        count_loop1 +=1
        count += 1
    print(f"Total iterations (two loops run one after another) count_loop1: {count_loop1}")

    count_loop2 = 0
    for j in range(1, n+1):
        count_loop2 +=1
        count += 1
    print(f"Total iterations (two loops run one after another) count_loop2: {count_loop2}")
    print(f"Total iterations (two loops run one after another): {count}")



def two_loops_nested(n):
    count = 0
    for i in range(1, n+1):
        count += 1
        for j in range (1, n+1):
            count += 1
    print(f"Total iterations (two loops nested): {count}")


# for n in range(10, 50, 10):
#     two_loops_run_one_after_another(n)
#     two_loops_nested(n)
two_loops_run_one_after_another(10)
two_loops_nested(10)

#Division & Halving → Logarithmic Thinking

#Start with a number n

#Repeatedly divide it by 2 until it reaches 1

#Count how many steps it takes

#Repeat for:

#n = 8

#n = 16

#n = 1024

#Write a sentence describing the relationship between input size and steps.

#small division program to start with

def divide(n):
    print(f"{n}/2 : {n/2}")

divide(8)
# divide(16)
# divide(1024)

def count_division_steps(n):
    count = 0
    m = n
    while n > 1:
        n = n / 2
        count += 1
    print(f"Total division steps for {m}: {count}")

count_division_steps(8)
# count_division_steps(16)
# count_division_steps(1024)



print("--------------------------------------------------------")

# Write:

# A loop that does only arithmetic

# A loop that calls a function

# Measure execution time

# Keep iteration count the same

# Observe the difference

# Write down:

# Which operation is more expensive

# Why that might matter in interviews


def arthematic_loop(n):
    total = 0
    for i in range(n):
        total += 1
    # if total > 0:
    #     print("Total (arithmetic loop):", total)

def function_call_loop(n):
    for i in range(n):
        arthematic_loop(i)
import time

def measure_execution_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    print(f"Execution time for {func.__name__} with n={n}: {end_time - start_time:.6f} seconds")
n = 100
measure_execution_time(arthematic_loop, n)
measure_execution_time(function_call_loop, n)