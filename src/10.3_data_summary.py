import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Optional: Set backend for PyCharm
matplotlib.use('TkAgg')

# Load the dataset
file_path = 'Cleaned_MaharashtraCovidCases.csv'  # Replace with your cleaned CSV file path
data = pd.read_csv(file_path)

# Enable interactive mode
plt.ion()

# Task 3: Data Aggregation
aggregated_data = None
if 'District' in data.columns and 'Cases' in data.columns:
    aggregated_data = data.groupby('District')['Cases'].sum().reset_index()
    print("\nAggregated Data (Total Cases by District):")
    print(aggregated_data)

# Task 4: Plotting Graphs
plt.style.use('ggplot')

# Line Plot
if 'Date' in data.columns and 'Cases' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])
    data_sorted = data.sort_values('Date')
    plt.figure(figsize=(10, 6))
    plt.plot(data_sorted['Date'], data_sorted['Cases'], marker='o', label='Cases Trend')
    plt.title("Trend of Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Bar Plot
if aggregated_data is not None:
    plt.figure(figsize=(10, 6))
    plt.bar(aggregated_data['District'], aggregated_data['Cases'], color='skyblue')
    plt.title("Total Cases by District")
    plt.xlabel("District")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Histogram
if 'Cases' in data.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(data['Cases'], bins=15, color='orange', edgecolor='black')
    plt.title("Distribution of Cases")
    plt.xlabel("Number of Cases")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Scatter Plot
if 'Cases' in data.columns and 'Deaths' in data.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Cases'], data['Deaths'], alpha=0.7, c='red')
    plt.title("Relationship Between Cases and Deaths")
    plt.xlabel("Number of Cases")
    plt.ylabel("Number of Deaths")
    plt.tight_layout()
    plt.show()