import pandas as pd

# Load the dataset
file_path = '10.1_MaharashtraLatestCovidCases.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Identify and handle missing values
print("\nMissing Values Count:")
print(data.isnull().sum())

# Handle missing values (example: drop rows with missing values)
data_cleaned = data.dropna()  # Alternatively, use data.fillna() for imputation

# Remove duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

# Display basic information about the cleaned dataset
print("\nData after cleaning:")
print(data_cleaned.info())

# Save the cleaned data to a new CSV file
cleaned_file_path = 'Cleaned_CovidCases.csv'  # Path to save the cleaned data
data_cleaned.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to: {cleaned_file_path}")
