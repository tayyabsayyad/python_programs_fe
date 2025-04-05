import re


def validate_url(url):
    """
    Validates if the given string is a valid URL.
    A valid URL should follow this format:
    - Protocol: http or https
    - Domain name: valid characters and extensions
    - Optional path, query parameters, and fragments
    """
    url_pattern = re.compile(
        r'^(https?://)'  # Protocol: http or https
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Domain extension
        r'(/[\w\-./?%&=]*)?$'  # Optional path and query parameters
    )
    if re.match(url_pattern, url):
        return True
    return False


def main():
    print("URL Validator")
    url = input("Enter a URL: ").strip()
    if validate_url(url):
        print(f"'{url}' is a valid URL.")
    else:
        print(
            f"'{url}' is not a valid URL. Please ensure it starts with http:// or https:// and has a valid domain name.")


if __name__ == "__main__":
    main()
