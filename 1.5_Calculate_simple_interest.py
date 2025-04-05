def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


print("Simple Interest Calculator")

try:
    # Input principal amount, rate of interest, and time period
    principal = float(input("Enter the principal amount (₹): "))
    rate = float(input("Enter the annual rate of interest (%): "))
    time = float(input("Enter the time period (in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative. Please enter valid positive values.")
        exit

    # Calculate simple interest
    simple_interest = calculate_simple_interest(principal, rate, time)

    # Display the result
    print(f"\nPrincipal Amount: ₹{principal:.2f}")
    print(f"Rate of Interest: {rate:.2f}%")
    print(f"Time Period: {time:.2f} years")
    print(f"Simple Interest: ₹{simple_interest:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for the inputs.")
