def fibonacci_sequence(limit):

    a, b = 0, 1  # Starting values of the sequence
    count = 0

    print(f"Fibonacci sequence with {limit} terms:")
    while count < limit:
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Update to the next term
        count += 1
    print()  # Newline for clean output


print("Fibonacci Sequence Generator")
try:
    terms = int(input("Enter the number of terms you want to print: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")

