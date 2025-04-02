# Function to check if a number is prime
def is_prime(n):
    # A prime number must be greater than or equal to 2
    if n < 2:
        return False
    
    # Check for factors from 2 to the square root of 'n'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If 'n' is divisible by 'i', it's not prime
            return False
    return True  # If no factors were found, the number is prime

# Accept a list of numbers from the user as input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Use list comprehension to filter only prime numbers from the input list
prime_numbers = [num for num in numbers if is_prime(num)]

# Print the list of prime numbers
print("Prime numbers:", prime_numbers)

