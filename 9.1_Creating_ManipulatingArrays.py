import numpy as np


# Create 1D, 2D, and 3D arrays
def create_arrays():
    # 1D Array
    array_1d = np.array([1, 2, 3, 4, 5])
    print("1D Array:")
    print(array_1d)

    # 2D Array
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D Array:")
    print(array_2d)

    # 3D Array
    array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("\n3D Array:")
    print(array_3d)

    return array_1d, array_2d, array_3d


# Reshaping arrays
def reshape_array(array):
    print("\nReshaping 1D Array:")
    reshaped = array.reshape((1, 5))  # Reshaping 1D array to 2D with 1 row and 5 columns
    print(reshaped)
    return reshaped


# Slicing arrays
def slice_array(array_2d):
    print("\nSlicing 2D Array:")
    print("Original Array:")
    print(array_2d)
    sliced = array_2d[0, 1:]  # Slicing first row, columns from index 1 onward
    print("Sliced Array (First row, from second column onward):")
    print(sliced)


# Indexing arrays
def index_array(array_3d):
    print("\nIndexing 3D Array:")
    print("Original Array:")
    print(array_3d)
    element = array_3d[1, 0, 2]  # Accessing element at depth 1, row 0, column 2
    print(f"Element at index [1, 0, 2]: {element}")


if __name__ == "__main__":
    # Create arrays
    array_1d, array_2d, array_3d = create_arrays()

    # Reshape the 1D array
    reshaped_1d = reshape_array(array_1d)

    # Slice the 2D array
    slice_array(array_2d)

    # Index into the 3D array
    index_array(array_3d)
