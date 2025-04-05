def check_even_or_odd():
    """Identify whether a number is even or odd."""
    while True:
        try:
            # Input the number
            num = int(input("\nEnter a number to check (or type 'exit' to quit): "))

            # Check if the number is even or odd
            if num % 2 == 0:
                print(f"{num} is an Even number.")
            else:
                print(f"{num} is an Odd number.")
        except ValueError:
            # Exit condition
            exit_prompt = input("Invalid input! Type 'exit' to quit or press Enter to continue: ").strip().lower()
            if exit_prompt == 'exit':
                print("Exiting the program. Goodbye!")
                break

print("Even or Odd Identifier")
check_even_or_odd()