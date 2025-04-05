import pandas as pd

# Load the Iris dataset
file_path = 'Iris.csv'  # Replace with the actual path to your Iris dataset
iris_data = pd.read_csv(file_path)

# Task i: Read the first 8 rows of the dataset
print("First 8 rows of the dataset:")
print(iris_data.head(8), "\n")

# Task ii: Display the column names of the Iris dataset
print("Column names:")
print(iris_data.columns.tolist(), "\n")

# Task iii: Fill any missing data with the mean value of the respective column
iris_filled = iris_data.fillna(iris_data.mean(numeric_only=True))
print("Dataset after filling missing values with the mean:\n")
print(iris_filled.head(8), "\n")

# Task iv: Remove rows that contain any missing values
iris_no_missing = iris_data.dropna()
print("Dataset after removing rows with missing values:")
print(iris_no_missing.head(8), "\n")

# Task v: Group the data by the species of the flower
grouped_data = iris_no_missing.groupby('Species')
print("Grouped data by species:")
print(grouped_data.size(), "\n")

# Task vi: Calculate and display mean, minimum, and maximum values of the Sepal length column
if 'sepal_length' in iris_data.columns:
    mean_sepal_length = iris_no_missing['sepal_length'].mean()
    min_sepal_length = iris_no_missing['sepal_length'].min()
    max_sepal_length = iris_no_missing['sepal_length'].max()

    print(f"Sepal Length Statistics:")
    print(f"Mean: {mean_sepal_length}")
    print(f"Minimum: {min_sepal_length}")
    print(f"Maximum: {max_sepal_length}")