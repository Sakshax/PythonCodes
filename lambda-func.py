"Lambda function is the anonymous function in Python. It is a small anonymous function that can take any number of arguments, but can only have one expression. It is used to create small, throwaway functions without having to formally define them using the def keyword."

welcome = lambda name: f"Hello, {name}!"
def greet(name):
    return welcome(name)

name = input("Enter your name: ")
print(greet(name))

# The above code defines a lambda function called welcome that takes a name as an argument and returns a greeting message.
# The greet function calls the welcome lambda function and returns the greeting message.
# The user is prompted to enter their name, and the greet function is called with the entered name.
# The greeting message is printed to the console.