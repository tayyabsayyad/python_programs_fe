
print("Basic Arithmetic Operations")

try:
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division by zero
    if num2 != 0:
        division = num1 / num2
        modulus = num1 % num2
    else:
        division = "Undefined (division by zero)"
        modulus = "Undefined (modulus by zero)"

    # Display results
    print("\nResults:")
    print(f"Addition ({num1} + {num2}): {addition}")
    print(f"Subtraction ({num1} - {num2}): {subtraction}")
    print(f"Multiplication ({num1} * {num2}): {multiplication}")
    print(f"Division ({num1} / {num2}): {division}")
    print(f"Modulus ({num1} % {num2}): {modulus}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
