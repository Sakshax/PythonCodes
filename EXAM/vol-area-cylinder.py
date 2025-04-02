import math

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def main():
    print("Cylinder Calculator")
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    
    print(f"Volume of the cylinder: {volume:.2f}")
    print(f"Surface area of the cylinder: {surface_area:.2f}")

if __name__ == "__main__":
    main()