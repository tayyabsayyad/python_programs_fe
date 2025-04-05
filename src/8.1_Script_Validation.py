import re


def validate_phone_number(phone):
    """
    Validates if the given phone number matches a standard format.
    Standard Format: 10 digits, optionally starting with +91 for India.
    """
    phone_pattern = r"^(\+91[-\s]?)?[6-9]\d{9}$"
    if re.match(phone_pattern, phone):
        return True
    return False


def validate_email(email):
    """
    Validates if the given email matches a standard email format.
    Standard Format: username@domain.extension
    """
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pattern, email):
        return True
    return False


def main():
    print("Phone Number and Email Validator")

    # Input for phone number
    phone = input("Enter your phone number: ").strip()
    if validate_phone_number(phone):
        print("Valid Phone Number.")
    else:
        print(
            "Invalid Phone Number. Please enter a valid 10-digit number starting with 6-9, optionally prefixed with +91.")

    # Input for email ID
    email = input("Enter your email ID: ").strip()
    if validate_email(email):
        print("Valid Email ID.")
    else:
        print("Invalid Email ID. Please enter a valid email address (e.g., example@domain.com).")


if __name__ == "__main__":
    main()
