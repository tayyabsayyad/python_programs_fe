import pandas as pd


def load_and_inspect_data(file_path):
    """
    Load a CSV file into a DataFrame, inspect its first few rows, data types, and basic statistics.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    None
    """
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)

        # Display the first few rows of the DataFrame
        print("First 5 rows of the dataset:")
        print(data.head(), "\n")

        # Display data types of each column
        print("Data Types:")
        print(data.dtypes, "\n")

        # Display basic statistics
        print("Summary Statistics:")
        print(data.describe(include='all'), "\n")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = "10.1_MaharashtraLatestCovidCases.csv"
load_and_inspect_data(file_path)
