# Run in Command line

import tkinter as tk
from tkinter import ttk


class ConversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Conversion Utility")
        self.root.geometry("400x300")

        # Title Label
        self.title_label = tk.Label(root, text="Unit Conversion Utility", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Input Field
        self.input_label = tk.Label(root, text="Enter Value:")
        self.input_label.pack()
        self.input_field = tk.Entry(root, font=("Arial", 12), justify="center")
        self.input_field.pack(pady=5)

        # Dropdown Menu for Conversion Type
        self.conversion_types = ["Currency: Rupees to Dollars", "Temperature: Celsius to Fahrenheit",
                                 "Length: Inches to Feet"]
        self.selected_conversion = tk.StringVar(value=self.conversion_types[0])
        self.dropdown = ttk.Combobox(root, textvariable=self.selected_conversion, values=self.conversion_types,
                                     state="readonly", font=("Arial", 12))
        self.dropdown.pack(pady=5)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert", command=self.perform_conversion,
                                        font=("Arial", 12, "bold"))
        self.convert_button.pack(pady=10)

        # Output Label
        self.output_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="red")
        self.output_label.pack(pady=10)

    def perform_conversion(self):
        try:
            # Get input value
            value = float(self.input_field.get())
            conversion_type = self.selected_conversion.get()
            result = ""

            # Perform conversion based on the selected type
            if conversion_type == "Currency: Rupees to Dollars":
                result = f"${value / 82.5:.2f} (at 1 USD = 82.5 INR)"
            elif conversion_type == "Temperature: Celsius to Fahrenheit":
                result = f"{(value * 9 / 5) + 32:.2f} °F"
            elif conversion_type == "Length: Inches to Feet":
                result = f"{value / 12:.2f} ft"
            else:
                result = "Invalid conversion type selected."

            # Display the result
            self.output_label.config(text=f"Result: {result}")
        except ValueError:
            self.output_label.config(text="Error: Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConversionApp(root)
    root.mainloop()