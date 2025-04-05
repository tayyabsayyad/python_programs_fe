import random


def number_guessing_game():
 
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    attempts = 0  # Count the number of attempts

    while True:
        try:
            # Take the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the user's guess
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")


while True:
    number_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break

