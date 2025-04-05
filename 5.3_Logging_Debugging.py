import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='banking_system.log',  # Log output file
    filemode='a'  # Append to the log file
)


class InvalidAccountNumberException(Exception):
    """Custom exception for invalid account numbers."""
    pass


class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    pass


class BankSystem:
    def __init__(self):
        self.accounts = {
            "12345": 5000,
            "67890": 10000,
            "54321": 2000
        }
        logging.info("BankSystem initialized with predefined accounts.")

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
        logging.debug(f"Attempting withdrawal: Account={account_number}, Amount={amount:.2f}")

        if account_number not in self.accounts:
            logging.error(f"Invalid account number: {account_number}")
            raise InvalidAccountNumberException(f"Account number {account_number} is invalid.")

        if amount > self.accounts[account_number]:
            logging.error(
                f"Insufficient funds for account: {account_number}, Requested: {amount:.2f}, Available: {self.accounts[account_number]:.2f}")
            raise InsufficientFundsException("Insufficient funds in the account.")

        self.accounts[account_number] -= amount
        logging.info(
            f"Withdrawal successful: Account={account_number}, Withdrawn={amount:.2f}, Remaining={self.accounts[account_number]:.2f}")
        print(f"Withdrawal successful! Remaining balance: {self.accounts[account_number]:.2f}")


def main():
    logging.info("Banking System started.")
    print("Welcome to the Banking System!")
    bank = BankSystem()

    while True:
        try:
            account_number = input("\nEnter your account number: ").strip()
            amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw_money(account_number, amount)

        except InvalidAccountNumberException as e:
            logging.warning(f"Handled InvalidAccountNumberException: {e}")
            print(f"Error: {e}")
        except InsufficientFundsException as e:
            logging.warning(f"Handled InsufficientFundsException: {e}")
            print(f"Error: {e}")
        except ValueError:
            logging.error("Invalid input! Non-numeric value entered.")
            print("Error: Invalid input! Please enter a numeric value for the amount.")
        except Exception as e:
            logging.critical(f"Unhandled exception: {e}")
            print(f"An unexpected error occurred: {e}")

        # Ask the user if they want to perform another transaction
        another_transaction = input("\nDo you want to make another transaction? (yes/no): ").strip().lower()
        if another_transaction != 'yes':
            logging.info("Banking System terminated by the user.")
            print("Thank you for using the Banking System. Goodbye!")
            break


if __name__ == "__main__":
    main()