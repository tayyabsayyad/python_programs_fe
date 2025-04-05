import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Toyota.csv'  # Replace with your file path
cars_data = pd.read_csv(file_path)

# Ensure data is loaded properly
print("First 5 rows of the dataset:")
print(cars_data.head(), "\n")

# Task i: Scatter plot between Age and Price
if 'Age' in cars_data.columns and 'Price' in cars_data.columns:
    plt.figure(figsize=(8, 6))
    plt.scatter(cars_data['Age'], cars_data['Price'], alpha=0.7, color='blue')
    plt.title("Scatter Plot: Age vs. Price of Cars")
    plt.xlabel("Age (Years)")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Task ii: Histogram for Kilometers driven
if 'KM' in cars_data.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(cars_data['KM'].dropna(), bins=15, color='green', edgecolor='black')
    plt.title("Histogram: Kilometers Driven")
    plt.xlabel("Kilometers Driven")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Task iii: Bar plot for distribution by fuel type
if 'FuelType' in cars_data.columns:
    fuel_counts = cars_data['FuelType'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(fuel_counts.index, fuel_counts.values, color='orange', edgecolor='black')
    plt.title("Bar Plot: Distribution of Cars by Fuel Type")
    plt.xlabel("Fuel Type")
    plt.ylabel("Count")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Task iv: Pie chart for percentage distribution by fuel type
if 'FuelType' in cars_data.columns:
    plt.figure(figsize=(8, 6))
    plt.pie(fuel_counts.values, labels=fuel_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'pink'])
    plt.title("Pie Chart: Percentage Distribution of Cars by Fuel Type")
    plt.tight_layout()
    plt.show()

# Task v: Box plot for car prices by fuel type
if 'FuelType' in cars_data.columns and 'Price' in cars_data.columns:
    plt.figure(figsize=(8, 6))
    cars_data.boxplot(column='Price', by='FuelType', grid=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    plt.title("Box Plot: Car Prices by Fuel Type")
    plt.suptitle("")  # Remove the automatic matplotlib title
    plt.xlabel("Fuel Type")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()