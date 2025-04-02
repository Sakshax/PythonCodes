# Program to swap the value of two variables

# Input two numbers from the user
a = int(input("Enter the first number: "))  # Taking first number as input
b = int(input("Enter the second number: "))  # Taking second number as input

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping the values using tuple unpacking
a, b = b, a  # Assigns 'b' to 'a' and 'a' to 'b' in a single step

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")
