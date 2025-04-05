import tkinter as tk
from tkinter import ttk
import math

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometric Area Calculator")
        self.root.geometry("400x400")

        # Title Label
        self.title_label = tk.Label(root, text="Geometric Area Calculator", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Dropdown Menu for Shape Selection
        self.shapes = ["Circle", "Rectangle", "Triangle"]
        self.selected_shape = tk.StringVar(value=self.shapes[0])
        self.dropdown = ttk.Combobox(root, textvariable=self.selected_shape, values=self.shapes, state="readonly", font=("Arial", 12))
        self.dropdown.pack(pady=10)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_fields)

        # Frame for Input Fields
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Input Fields
        self.labels = []
        self.entries = []

        # Result Label
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="red")
        self.result_label.pack(pady=10)

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate Area", command=self.calculate_area, font=("Arial", 12, "bold"))
        self.calculate_button.pack(pady=10)

        self.update_fields()  # Initialize input fields based on the default shape

    def update_fields(self, event=None):
        # Clear existing input fields
        for label in self.labels:
            label.destroy()
        for entry in self.entries:
            entry.destroy()
        self.labels.clear()
        self.entries.clear()

        # Update input fields based on the selected shape
        shape = self.selected_shape.get()
        if shape == "Circle":
            self.add_input_field("Radius:")
        elif shape == "Rectangle":
            self.add_input_field("Length:")
            self.add_input_field("Width:")
        elif shape == "Triangle":
            self.add_input_field("Base:")
            self.add_input_field("Height:")

    def add_input_field(self, label_text):
        label = tk.Label(self.input_frame, text=label_text, font=("Arial", 12))
        label.pack()
        self.labels.append(label)

        entry = tk.Entry(self.input_frame, font=("Arial", 12), justify="center")
        entry.pack(pady=5)
        self.entries.append(entry)

    def calculate_area(self):
        try:
            # Retrieve input values
            values = [float(entry.get()) for entry in self.entries]
            shape = self.selected_shape.get()
            area = 0

            # Calculate area based on the shape
            if shape == "Circle":
                radius = values[0]
                area = math.pi * radius ** 2
            elif shape == "Rectangle":
                length, width = values
                area = length * width
            elif shape == "Triangle":
                base, height = values
                area = 0.5 * base * height

            # Display the result
            self.result_label.config(text=f"Result: {area:.2f} square units")
        except ValueError:
            self.result_label.config(text="Error: Please enter valid numbers.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()