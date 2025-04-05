def is_prime(number):
    if number <= 1:
        return False  # Numbers <= 1 are not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, not a prime number
    return True


print("Prime Number Checker")
try:
    # Input the number
    num = int(input("Enter an integer to check if it's prime: "))

    # Analyze if the number is prime
    if is_prime(num):
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is not a Prime number.")
except ValueError:
    print("Invalid input! Please enter an integer.")

