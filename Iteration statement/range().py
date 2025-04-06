# The range() function in Python is used to generate a sequence of numbers.
# It is commonly used in loops to iterate over a block of code a specific number of times.

# Syntax:
# range(start, stop, step)

# Parameters:
# start: Optional. The starting value of the sequence. Default is 0.
# stop: Required. The sequence ends before this value.
# step: Optional. The difference between each number in the sequence. Default is 1.

# Examples:

# Example 1: Using range() with only the stop parameter
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

# Example 2: Using range() with start and stop parameters
for i in range(2, 7):  # Generates numbers from 2 to 6
    print(i)

# Example 3: Using range() with start, stop, and step parameters
for i in range(1, 10, 2):  # Generates numbers 1, 3, 5, 7, 9
    print(i)

# Example 4: Using range() with a negative step
for i in range(10, 0, -2):  # Generates numbers 10, 8, 6, 4, 2
    print(i)