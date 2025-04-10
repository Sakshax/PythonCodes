def get_division(percentage):
    if percentage >= 75:
        return "First class with distinction"
    elif percentage >= 60:
        return "First class"
    elif percentage >= 45:
        return "Second class"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def main():
    marks = []
    print("Enter marks for 5 subjects (out of 100):")
    
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks)
    percentage = total / 5

    print(f"\nTotal Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Division: {get_division(percentage)}")

if __name__ == "__main__":
    main()
