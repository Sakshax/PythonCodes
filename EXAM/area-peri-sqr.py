def calculate_square_properties(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

side_length = float(input("Enter the side length of the square: "))
if side_length > 0:
    area, perimeter = calculate_square_properties(side_length)
    print(f"Area: {area}, Perimeter: {perimeter}")
else:
    print("Side length must be positive.")
