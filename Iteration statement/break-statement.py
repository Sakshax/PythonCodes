# The break statement in Python is used to exit a loop prematurely.
# It is commonly used when a certain condition is met, and you want to stop the loop execution.

# Example: Using break in a for loop
for number in range(1, 10):
    if number == 5:
        print("Breaking the loop as number is", number)
        break
    print("Current number is", number)

# Example: Using break in a while loop
count = 0
while count < 10:
    if count == 7:
        print("Breaking the loop as count is", count)
        break
    print("Current count is", count)
    count += 1