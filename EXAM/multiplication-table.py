# Program to print the multiplication table of a given number

def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print_multiplication_table(num)
    except ValueError:
        print("Please enter a valid integer.")