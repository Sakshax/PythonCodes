 # Arithmetic operators
x = 10
y = 5
print(x + y)  # Addition: Adds two operands # Output: 15
print(x - y)  # Subtraction: Subtracts two operands # Output: 5
print(x * y)  # Multiplication: Multiplies two operands # Output: 50
print(x / y)  # Division: Divides the first operand by the second # Output: 2.0
print(x % y)  # Modulus: Returns the remainder after division # Output: 0
print(x ** y) # Exponentiation: Raises the first operand to the power of the second # Output: 100000
print(x // y) # Floor division: Divides and returns the integer part of the quotient # Output: 2

# Assignment operators
x = 5
x += 3 # Equivalent to x = x + 3
print(x) # Output: 8
x -= 2 # Equivalent to x = x - 2
print(x) # Output: 6
x *= 4 # Equivalent to x = x * 4
print(x) # Output: 24
x /= 2 # Equivalent to x = x / 2
print(x) # Output: 12.0
x %= 3 # Equivalent to x = x % 3
print(x) # Output: 0.0
x **= 2 # Equivalent to x = x ** 2
print(x) # Output: 0.0
x //= 3 # Equivalent to x = x // 3
print(x) # Output: 0.0

# Comparison operators
x = 5
y = 10
print(x == y) # Equal to: Returns True if both operands are equal # Output: False
print(x != y) # Not equal to: Returns True if operands are not equal # Output: True
print(x > y)  # Greater than: Returns True if the left operand is greater than the right # Output: False
print(x < y)  # Less than: Returns True if the left operand is less than the right # Output: True
print(x >= y) # Greater than or equal to: Returns True if the left operand is greater than or equal to the right # Output: False
print(x <= y) # Less than or equal to: Returns True if the left operand is less than or equal to the right # Output: True

# Logical operators
x = True
y = False
print(x and y) # Logical AND: Returns True if both operands are True # Output: False
print(x or y)  # Logical OR: Returns True if at least one operand is True # Output: True
print(not x)   # Logical NOT: Returns True if the operand is False # Output: False

# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)    # Returns True if both variables are the same object # Output: False
print(x is not y)# Returns True if both variables are not the same object # Output: True
print(x is z)    # Returns True because z is a reference to x # Output: True

# Membership operators
x = [1, 2, 3]
print(1 in x)    # Returns True if a sequence with the specified value is present in the object # Output: True
print(4 not in x) # Returns True if a sequence with the specified value is not present in the object # Output: True

# Bitwise operators
x = 10 # 1010 in binary
y = 4  # 0100 in binary
print(x & y)  # Bitwise AND: Sets each bit to 1 if both bits are 1 # Output: 0
print(x | y)  # Bitwise OR: Sets each bit to 1 if one of two bits is 1 # Output: 14
print(x ^ y)  # Bitwise XOR: Sets each bit to 1 if only one of two bits is 1 # Output: 14
print(~x)   # Bitwise NOT: Inverts all the bits # Output: -11
print(x << 2) # Left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off # Output: 40
print(x >> 2) # Right shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off # Output: 2