import numpy as np

def array_operations():
    # Create two arrays of the same shape
    array1 = np.array([10, 20, 30, 40, 50])
    array2 = np.array([1, 2, 3, 4, 5])

    print("Array 1:", array1)
    print("Array 2:", array2)

    # Element-wise operations
    addition = array1 + array2
    subtraction = array1 - array2
    multiplication = array1 * array2
    division = array1 / array2

    print("\nElement-wise Addition:", addition)
    print("Element-wise Subtraction:", subtraction)
    print("Element-wise Multiplication:", multiplication)
    print("Element-wise Division:", division)

    # Dot product (arrays must be vectors of the same length)
    dot_product = np.dot(array1, array2)
    print("\nDot Product:", dot_product)

    # Cross product (arrays must be vectors of size 3)
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    cross_product = np.cross(vector1, vector2)

    print("\nVector 1:", vector1)
    print("Vector 2:", vector2)
    print("Cross Product:", cross_product)

if __name__ == "__main__":
    array_operations()