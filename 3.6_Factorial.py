def factorial(n):

    if n == 0 or n == 1:
        return 1  # Factorial of 0 or 1 is 1
    result = 1
    for i in range(2, n + 1):
        result *= i  # Multiply each number from 2 to n
    return result


print("Factorial Calculator")
try:
    # Input the integer
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Compute factorial
        fact = factorial(num)
        print(f"The factorial of {num} is: {fact}")
except ValueError:
    print("Invalid input! Please enter a non-negative integer.")

