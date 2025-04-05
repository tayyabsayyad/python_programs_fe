import re


def extract_data_from_file(file_path):
    """
    Reads a text file and extracts emails, phone numbers, and dates using regular expressions.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Regular expressions for different data types
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_pattern = r'\b(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
        date_pattern = r'\b(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}\b'

        # Extract data using the patterns
        emails = re.findall(email_pattern, content)
        phone_numbers = re.findall(phone_pattern, content)
        dates = re.findall(date_pattern, content)

        # Display extracted data
        print("Extracted Emails:")
        for email in emails:
            print(email)

        print("\nExtracted Phone Numbers:")
        for phone in phone_numbers:
            print(phone)

        print("\nExtracted Dates:")
        for date in dates:
            print(date)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Data Extraction from Text File")
    file_path = input("Enter the path to the text file: ").strip()
    extract_data_from_file(file_path)


if __name__ == "__main__":
    main()
