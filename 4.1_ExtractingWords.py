import string


def extract_words_by_length(file_path, word_length):
    """
    Extract and print words of a specific length from a text file.
    :param file_path: Path to the text file
    :param word_length: Length of words to extract
    """
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            content = file.read()

        # Remove punctuation using str.translate
        translator = str.maketrans('', '', string.punctuation)
        clean_content = content.translate(translator)

        # Split the text into words
        words = clean_content.split()

        # Filter words by specified length
        matching_words = [word for word in words if len(word) == word_length]

        # Display results
        if matching_words:
            print(f"Words of length {word_length}:")
            print(", ".join(matching_words))
        else:
            print(f"No words of length {word_length} found in the file.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# User inputs
file_path = input("Enter File Handling- Reading and writing files")

try:
    word_length = int(input("Enter the word length to extract: "))
    if word_length < 1:
        print("Word length must be greater than 0.")
    else:
        extract_words_by_length(file_path, word_length)
except ValueError:
    print("Please enter a valid number for the word length.")