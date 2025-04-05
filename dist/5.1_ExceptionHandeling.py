def divide_numbers():
    """
    Prompt the user for two numbers and perform division.
    Handle division by zero and invalid input errors gracefully.
    """
    try:
        # Take input for the numerator and denominator
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform division and print the result
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is {result:.2f}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Division Program with Exception Handling")
    while True:
        divide_numbers()
        try_again = input("Do you want to perform another division? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you for using the division program. Goodbye!")
            break

if __name__ == "__main__":
    main()