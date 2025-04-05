def multiplication_table(number, limit=10):

    print(f"\nMultiplication Table for {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


print("Multiplication Table Generator")
try:
    # Input the number for which the multiplication table is needed
    num = int(input("Enter a number: "))

    # Optional: Input the range of the table
    limit = input("Enter the range (default is 10): ").strip()
    if limit.isdigit():
        limit = int(limit)
    else:
        limit = 10

    multiplication_table(num, limit)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

