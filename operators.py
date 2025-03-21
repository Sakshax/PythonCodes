# Arithmetic Operators
"""
This script demonstrates the usage of various operators in Python, including arithmetic, assignment, relational, logical, and bitwise operators. Each operation is performed with example values and the results are printed with descriptive comments.

Operators covered:
1. Arithmetic Operators:
    - Addition: Adds two operands.
    - Subtraction: Subtracts the second operand from the first.
    - Multiplication: Multiplies two operands.
    - Division: Divides the first operand by the second.
    - Modulus: Returns the remainder when the first operand is divided by the second.
    - Exponentiation: Raises the first operand to the power of the second.
    - Floor Division: Divides the first operand by the second and returns the largest integer less than or equal to the result.

2. Assignment Operators:
    - Add AND (+=): Adds the right operand to the left operand and assigns the result to the left operand.
    - Subtract AND (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
    - Multiply AND (*=): Multiplies the left operand by the right operand and assigns the result to the left operand.
    - Divide AND (/=): Divides the left operand by the right operand and assigns the result to the left operand.
    - Modulus AND (%=): Takes modulus using two operands and assigns the result to the left operand.
    - Exponent AND (**=): Performs exponential (power) calculation on operators and assigns the result to the left operand.
    - Floor Division AND (//=): Performs floor division on operators and assigns the result to the left operand.

3. Relational Operators:
    - Equal to (==): Checks if the values of two operands are equal.
    - Not equal to (!=): Checks if the values of two operands are not equal.
    - Greater than (>): Checks if the value of the left operand is greater than the value of the right operand.
    - Less than (<): Checks if the value of the left operand is less than the value of the right operand.
    - Greater than or equal to (>=): Checks if the value of the left operand is greater than or equal to the value of the right operand.
    - Less than or equal to (<=): Checks if the value of the left operand is less than or equal to the value of the right operand.

4. Logical Operators:
    - Logical AND (and): Returns True if both operands are true.
    - Logical OR (or): Returns True if at least one of the operands is true.
    - Logical NOT (not): Reverses the logical state of its operand.

5. Bitwise Operators:
    - Bitwise AND (&): Performs bitwise AND operation on the operands.
    - Bitwise OR (|): Performs bitwise OR operation on the operands.
    - Bitwise XOR (^): Performs bitwise XOR operation on the operands.
    - Bitwise NOT (~): Performs bitwise NOT operation on the operand.
    - Bitwise left shift (<<): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
    - Bitwise right shift (>>): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.

Each section includes example operations with variables and the output of each operation is provided in comments for clarity.
"""
a = 10
b = 5

print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")  # Addition: 10 + 5 = 15
print(f"Subtraction: {a} - {b} = {a - b}")  # Subtraction: 10 - 5 = 5
print(f"Multiplication: {a} * {b} = {a * b}")  # Multiplication: 10 * 5 = 50
print(f"Division: {a} / {b} = {a / b}")  # Division: 10 / 5 = 2.0
print(f"Modulus: {a} % {b} = {a % b}")  # Modulus: 10 % 5 = 0
print(f"Exponentiation: {a} ** {b} = {a ** b}")  # Exponentiation: 10 ** 5 = 100000
print(f"Floor Division: {a} // {b} = {a // b}")  # Floor Division: 10 // 5 = 2

# Assignment Operators
c = a
print("\nAssignment Operators:")
c += b
print(f"Add AND: c += {b} -> c = {c}")  # Add AND: c += 5 -> c = 15
c -= b
print(f"Subtract AND: c -= {b} -> c = {c}")  # Subtract AND: c -= 5 -> c = 10
c *= b
print(f"Multiply AND: c *= {b} -> c = {c}")  # Multiply AND: c *= 5 -> c = 50
c /= b
print(f"Divide AND: c /= {b} -> c = {c}")  # Divide AND: c /= 5 -> c = 10.0
c %= b
print(f"Modulus AND: c %= {b} -> c = {c}")  # Modulus AND: c %= 5 -> c = 0.0
c **= b
print(f"Exponent AND: c **= {b} -> c = {c}")  # Exponent AND: c **= 5 -> c = 0.0
c //= b
print(f"Floor Division AND: c //= {b} -> c = {c}")  # Floor Division AND: c //= 5 -> c = 0.0

# Relational Operators
print("\nRelational Operators:")
print(f"Equal to: {a} == {b} -> {a == b}")  # Equal to: 10 == 5 -> False
print(f"Not equal to: {a} != {b} -> {a != b}")  # Not equal to: 10 != 5 -> True
print(f"Greater than: {a} > {b} -> {a > b}")  # Greater than: 10 > 5 -> True
print(f"Less than: {a} < {b} -> {a < b}")  # Less than: 10 < 5 -> False
print(f"Greater than or equal to: {a} >= {b} -> {a >= b}")  # Greater than or equal to: 10 >= 5 -> True
print(f"Less than or equal to: {a} <= {b} -> {a <= b}")  # Less than or equal to: 10 <= 5 -> False

# Logical Operators
x = True
y = False
print("\nLogical Operators:")
print(f"Logical AND: {x} and {y} -> {x and y}")  # Logical AND: True and False -> False
print(f"Logical OR: {x} or {y} -> {x or y}")  # Logical OR: True or False -> True
print(f"Logical NOT: not {x} -> {not x}")  # Logical NOT: not True -> False

# Bitwise Operators
print("\nBitwise Operators:")
print(f"Bitwise AND: {a} & {b} -> {a & b}")  # Bitwise AND: 10 & 5 -> 0
print(f"Bitwise OR: {a} | {b} -> {a | b}")  # Bitwise OR: 10 | 5 -> 15
print(f"Bitwise XOR: {a} ^ {b} -> {a ^ b}")  # Bitwise XOR: 10 ^ 5 -> 15
print(f"Bitwise NOT: ~{a} -> {~a}")  # Bitwise NOT: ~10 -> -11
print(f"Bitwise left shift: {a} << 1 -> {a << 1}")  # Bitwise left shift: 10 << 1 -> 20
print(f"Bitwise right shift: {a} >> 1 -> {a >> 1}")  # Bitwise right shift: 10 >> 1 -> 5