def check_character_type(char):
    if char.isdigit():
        print(f"'{char}' is a Digit.")
    elif char.islower():
        print(f"'{char}' is a Lowercase Letter.")
    elif char.isupper():
        print(f"'{char}' is an Uppercase Letter.")
    else:
        print(f"'{char}' is a Special Character.")


print("Character Type Identifier")
char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter only one character.")
else:
    check_character_type(char)

