import numpy as np


def statistical_operations():
    # Input array
    data = np.array([10, 20, 30, 40, 50])
    print("Data Array:", data)

    # Calculate mean
    mean = np.mean(data)
    print("\nMean:", mean)

    # Calculate median
    median = np.median(data)
    print("Median:", median)

    # Calculate standard deviation
    std_dev = np.std(data)
    print("Standard Deviation:", std_dev)

    # Calculate variance
    variance = np.var(data)
    print("Variance:", variance)

    # Correlation coefficients
    # Creating a second dataset for correlation calculation
    data2 = np.array([15, 25, 35, 45, 55])
    correlation = np.corrcoef(data, data2)
    print("\nData 1:", data)
    print("Data 2:", data2)
    print("Correlation Coefficient Matrix:\n", correlation)


if __name__ == "__main__":
    statistical_operations()
