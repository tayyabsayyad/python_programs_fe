def rupees_to_dollars(rupees, exchange_rate=82.50):
    return rupees / exchange_rate


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def inches_to_feet(inches):
    return inches / 12


while True:
    print("\nConversion Menu")
    print("1. Convert Rupees to Dollars")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Fahrenheit to Celsius")
    print("4. Convert Inches to Feet")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        rupees = float(input("Enter the amount in Rupees: "))
        dollars = rupees_to_dollars(rupees)
        print(f"{rupees} Rupees is equivalent to ${dollars:.2f}.")

    elif choice == '2':
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F.")

    elif choice == '3':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C.")

    elif choice == '4':
        inches = float(input("Enter the length in Inches: "))
        feet = inches_to_feet(inches)
        print(f"{inches} Inches is equivalent to {feet:.2f} Feet.")

    elif choice == '5':
        print("Exiting the converter. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
