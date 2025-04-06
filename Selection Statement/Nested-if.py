# Nested if example in Python

# Input from the user
number = int(input("Enter a number: "))

# Outer if statement
if number > 0:
    print("The number is positive.")
    
    # Nested if statement
    if number % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is not positive.")