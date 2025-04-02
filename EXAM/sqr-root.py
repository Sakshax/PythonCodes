import math

def find_square_root(number):
    return math.sqrt(number) if number >= 0 else "Undefined for negative numbers"

# Example usage
if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        print(find_square_root(num))
    except ValueError:
        print("Invalid input")
