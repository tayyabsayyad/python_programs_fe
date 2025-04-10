import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2


def calculate_rectangle_area(length, width):
    return length * width

    
def calculate_triangle_area(base, height):  
    return 0.5 * base * height

print("Geometric Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Choose a geometric figure (1/2/3): ")

if choice == '1':
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle is: {area:.2f}")
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area:.2f}")
elif choice == '3':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Invalid choice. Please select a valid option.")


