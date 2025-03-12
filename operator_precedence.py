# Operator precedence example
result = 10 + 2 * 5  # Multiplication is performed before addition
print("10 + 2 * 5 =", result)  # Output: 20

result = (10 + 2) * 5  # Parentheses change the order of operations
print("(10 + 2) * 5 =", result)  # Output: 60

result = 2 ** 3 * 4  # Exponentiation is performed before multiplication
print("2 ** 3 * 4 =", result)  # Output: 32

result = 2 ** (3 * 4)  # Parentheses change the order of operations
print("2 ** (3 * 4) =", result)  # Output: 4096