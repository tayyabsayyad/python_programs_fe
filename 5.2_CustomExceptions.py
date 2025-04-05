class InvalidAccountNumberException(Exception):
    """Custom exception for invalid account numbers."""
    pass


class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    pass


class BankSystem:
    def __init__(self):
        # A sample database of account numbers and balances
        self.accounts = {
            "12345": 5000,
            "67890": 10000,
            "54321": 2000
        }

    def withdraw_money(self, account_number, amount):
        """
        Withdraw money from a specified account.

        Parameters:
            account_number (str): The account number.
            amount (float): The amount to withdraw.

        Raises:
            InvalidAccountNumberException: If the account number does not exist.
            InsufficientFundsException: If there are insufficient funds in the account.
        """
        if account_number not in self.accounts:
            raise InvalidAccountNumberException(f"Account number {account_number} is invalid.")

        if amount > self.accounts[account_number]:
            raise InsufficientFundsException("Insufficient funds in the account.")

        self.accounts[account_number] -= amount
        print(f"Withdrawal successful! Remaining balance: {self.accounts[account_number]:.2f}")



print("Welcome to the Banking System!")
bank = BankSystem()

while True:
    try:
        account_number = input("\nEnter your account number: ").strip()
        amount = float(input("Enter the amount to withdraw: "))
        bank.withdraw_money(account_number, amount)

    except InvalidAccountNumberException as e:
        print(f"Error: {e}")
    except InsufficientFundsException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input! Please enter a numeric value for the amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Ask the user if they want to perform another transaction
    another_transaction = input("\nDo you want to make another transaction? (yes/no): ").strip().lower()
    if another_transaction != 'yes':
        print("Thank you for using the Banking System. Goodbye!")
        break

