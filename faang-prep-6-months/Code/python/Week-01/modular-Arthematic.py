#  Experiment 1 (you write the code)

# Goal: Observe how modulo maps many numbers into few buckets

# Task:

# Create a list of size 5

# Insert numbers 0–20 using % 5

# Print which numbers land in which index


my_list = [None] * 5
for i in range(21):
    index= i % 5
    my_list[index] = i
    print(f"inserting {index} : {i}")


# 🔬 Experiment 2 (collision observation)

# Task:

# Use bucket size = 5

# Insert values that differ by 5 (e.g., 1, 6, 11, 16)

my_bucket = [None] * 5
for i in range(1, 17, 5):
    index = i % 5
    my_bucket[index] = i
    print(f"inserting in bucket {index} : {i}")

