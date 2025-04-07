# The 'continue' statement in Python is used to skip the rest of the code inside a loop
# for the current iteration and move to the next iteration of the loop.

# Example: Using 'continue' in a for loop
for number in range(1, 6):
    if number == 3:
        continue  # Skip the rest of the loop when number is 3
    print(f"Number: {number}")

# Output:
# Number: 1
# Number: 2
# Number: 4
# Number: 5