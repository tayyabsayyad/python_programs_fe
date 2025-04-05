import tkinter as tk
from tkinter import messagebox


class CollegeAdmissionForm:
    def __init__(self, root):
        self.root = root
        self.root.title("College Admission Registration Form")
        self.root.geometry("500x400")

        # Title Label
        self.title_label = tk.Label(root, text="College Admission Form", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Name Input
        self.name_label = tk.Label(root, text="Name:", font=("Arial", 12))
        self.name_label.pack(anchor="w", padx=20)
        self.name_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=5)

        # Branch Selection using Radio Buttons
        self.branch_label = tk.Label(root, text="Select Branch:", font=("Arial", 12))
        self.branch_label.pack(anchor="w", padx=20)
        self.branch_var = tk.StringVar(value="None")
        branches = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"]
        self.branch_radiobuttons = []
        for branch in branches:
            rb = tk.Radiobutton(root, text=branch, variable=self.branch_var, value=branch, font=("Arial", 10))
            rb.pack(anchor="w", padx=40)
            self.branch_radiobuttons.append(rb)

        # Favorite Sports Selection using Checkboxes
        self.sports_label = tk.Label(root, text="Select Favorite Sports:", font=("Arial", 12))
        self.sports_label.pack(anchor="w", padx=20)
        self.sports_vars = {}
        sports = ["Football", "Cricket", "Basketball", "Tennis", "Badminton"]
        for sport in sports:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(root, text=sport, variable=var, font=("Arial", 10))
            cb.pack(anchor="w", padx=40)
            self.sports_vars[sport] = var

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.display_output, font=("Arial", 12, "bold"))
        self.submit_button.pack(pady=10)

        # Output Label
        self.output_label = tk.Label(root, text="", font=("Arial", 12), fg="red", justify="left")
        self.output_label.pack(pady=10)

    def display_output(self):
        # Retrieve input values
        name = self.name_entry.get().strip()
        branch = self.branch_var.get()
        selected_sports = [sport for sport, var in self.sports_vars.items() if var.get()]

        # Validate inputs
        if not name or branch == "None" or not selected_sports:
            messagebox.showerror("Input Error", "Please fill all fields and select at least one sport.")
            return

        # Display the output
        sports_list = ", ".join(selected_sports)
        self.output_label.config(
            text=(
                f"Thank you for registering!\n\n"
                f"Name: {name}\n"
                f"Branch: {branch}\n"
                f"Favorite Sports: {sports_list}"
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeAdmissionForm(root)
    root.mainloop()
