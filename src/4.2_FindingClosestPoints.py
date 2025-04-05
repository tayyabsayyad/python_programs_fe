import csv
from math import sqrt


def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 3D space.

    Parameters:
        point1 (tuple): Coordinates of the first point (x1, y1, z1).
        point2 (tuple): Coordinates of the second point (x2, y2, z2).

    Returns:
        float: The distance between the two points.
    """
    return sqrt((point1[0] - point2[0]) ** 2 +
                (point1[1] - point2[1]) ** 2 +
                (point1[2] - point2[2]) ** 2)


def find_closest_points(points):
    """
    Find the two closest points from a list of points in 3D space.

    Parameters:
        points (list): List of points as tuples (x, y, z).

    Returns:
        tuple: The closest points and their distance.
    """
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance


def read_csv_coordinates(filename):
    """
    Read coordinates from a CSV file.

    Parameters:
        filename (str): The path to the CSV file.

    Returns:
        list: A list of points as tuples (x, y, z).
    """
    points = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                points.append(tuple(map(float, row)))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return points


print("Closest Points Finder in 3D Space")

filename = input("Enter the CSV file name (with extension): ").strip()
points = read_csv_coordinates(filename)

if len(points) < 2:
    print("The file must contain at least two points.")
    exit (0)

closest_pair, min_distance = find_closest_points(points)

print("\nThe two closest points are:")
print(f"Point 1: {closest_pair[0]}")
print(f"Point 2: {closest_pair[1]}")
print(f"Their distance: {min_distance:.6f}")
