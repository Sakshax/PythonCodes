def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def divide_complex(c1, c2):
    try:
        return c1 / c2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def main():
    print("Enter first complex number:")
    real1 = float(input("Real part: "))
    imag1 = float(input("Imaginary part: "))
    c1 = complex(real1, imag1)

    print("\nEnter second complex number:")
    real2 = float(input("Real part: "))
    imag2 = float(input("Imaginary part: "))
    c2 = complex(real2, imag2)

    while True:
        print("\n--- Complex Number Operations Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            result = add_complex(c1, c2)
            print(f"Result of addition: {result}")
        elif choice == '2':
            result = subtract_complex(c1, c2)
            print(f"Result of subtraction: {result}")
        elif choice == '3':
            result = multiply_complex(c1, c2)
            print(f"Result of multiplication: {result}")
        elif choice == '4':
            result = divide_complex(c1, c2)
            print(f"Result of division: {result}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
