
# Sample Program with Intentional Errors

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    total = 0
    count = len(numbers)  # Intentional error: What if numbers is an empty list?
    for num in numbers:
        total += num
    average = total / count  # Potential division by zero error
    return average


def main():
    """
    Main function to demonstrate the program.
    """
    sample_data = []  # Try using an empty list here to trigger an error
    print("Sample Data:", sample_data)
    result = calculate_average(sample_data)  # Incorrect handling of empty data
    print("Average:", result)


if __name__ == "__main__":
    main()


