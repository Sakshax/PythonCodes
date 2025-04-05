""" Basic Building Block of Python : Identifier, Keywords, Literals, Identation , Comments"""

""" 1. Identifier:
    - An identifier is a name given to entities like class, functions, variables, etc.
    - It helps to differentiate one entity from another.
    - Rules for naming identifiers:
        1. An identifier can only contain letters (a-z, A-Z), digits (0-9), or underscores (_).
        2. An identifier cannot start with a digit.
        3. An identifier cannot be a keyword in Python.
        4. Identifiers are case-sensitive.
        5. Identifiers should be meaningful and descriptive.
"""
# Example of identifiers
my_variable = 10  # variable identifier
def my_function():  # function identifier
    pass

class MyClass:  # class identifier
    pass

# Example of invalid identifiers
# 1my_variable = 20  # cannot start with a digit
# my-variable = 30  # cannot contain hyphen
# my variable = 40  # cannot contain spaces
# my@variable = 50  # cannot contain special characters





""" 2. Keywords:
    - Keywords are reserved words in Python that have a specific meaning and cannot be used as identifiers.
    - They are used to define the syntax and structure of the Python language.
    - There are 35 keywords in Python.
"""

# Example of keywords
import keyword
print("Python Keywords:")
print(keyword.kwlist)  # prints all the keywords in Python


# Example of using keywords
if True:
    print("This is an if statement.")
# Example of invalid keyword usage
# def = 5  # cannot use keyword 'def' as an identifier



""" 3. Literals:
    - Literals are fixed values that are represented directly in the code.
    - They can be of different types: string literals, numeric literals, boolean literals, etc.
"""

# Example of literals
string_literal = "Hello, World!"  # string literal
numeric_literal = 42  # numeric literal
boolean_literal = True  # boolean literal

# Example of different types of literals
integer_literal = 10  # integer literal
float_literal = 3.14  # float literal   
complex_literal = 2 + 3j  # complex literal
list_literal = [1, 2, 3]  # list literal
tuple_literal = (1, 2, 3)  # tuple literal
dict_literal = {"key": "value"}  # dictionary literal
set_literal = {1, 2, 3}  # set literal

# Example of invalid literal usage
# invalid_literal = 10.5.3  # invalid float literal     
# invalid_literal = "Hello'  # invalid string literal
# invalid_literal = [1, 2, 3,]  # invalid list literal

""" 4. Indentation:
    - Indentation is the whitespace at the beginning of a line.
    - It is used to define the structure and hierarchy of the code.
    - In Python, indentation is mandatory and is used to indicate blocks of code.
    - The standard indentation level is 4 spaces.
"""
# Example of indentation
def my_function():
    if True:
        print("This is inside the if statement.")
    else:
        print("This is inside the else statement.")

# Example of invalid indentation
# def my_function():
# print("This is inside the function.")  # invalid indentation
# Example of inconsistent indentation
# def my_function():
#     if True:
#         print("This is inside the if statement.")
#     else:         
#         print("This is inside the else statement.")  # inconsistent indentation


""" 5. Comments:
    - Comments are used to explain the code and make it more readable.
    - They are ignored by the Python interpreter.
    - There are two types of comments in Python: single-line comments and multi-line comments.
"""

# Example of single-line comment
# This is a single-line comment

# Example of multi-line comment
"""
This is a multi-line comment.
It can span multiple lines.
"""

# Example of inline comment
x = 10  # This is an inline comment
 
# Example of docstring comment
def my_function():
    """
    This is a docstring comment.
    It describes the purpose of the function.
    """
    pass

# Example of invalid comment usage
# # This is an invalid comment  # invalid comment usage
# # This is another invalid comment  # invalid comment usage
