import re


def validate_password(password):
    """
    Validates a password based on strength criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Strong Password!"


def main():
    print("Password Strength Checker")
    password = input("Enter your password: ").strip()
    validation_result = validate_password(password)
    print(validation_result)


if __name__ == "__main__":
    main()
