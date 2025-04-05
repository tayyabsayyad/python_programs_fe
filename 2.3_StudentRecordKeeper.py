def display_students(records):
    """Display all student records."""
    if not records:
        print("\nNo student records found.")
    else:
        print("\nStudent Records:")
        for roll, info in records.items():
            print(f"  Roll No: {roll}")
            print(f"  Name: {info['name']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Attendance: {info['attendance']}%")


def add_student(records):
    """Add a new student record."""
    roll = input("Enter the Roll Number: ").strip()
    if roll in records:
        print("A student with this roll number already exists.")
        return
    name = input("Enter the Student's Name: ").strip()
    grade = input("Enter the Grade: ").strip()
    try:
        attendance = float(input("Enter Attendance Percentage: "))
        if attendance < 0 or attendance > 100:
            print("Attendance must be between 0 and 100.")
            return
        records[roll] = {"name": name, "grade": grade, "attendance": attendance}
        print("Student added successfully.")
    except ValueError:
        print("Invalid input! Attendance must be a number.")


def update_student(records):
    """Update an existing student's record."""
    roll = input("Enter the Roll Number to update: ").strip()
    if roll not in records:
        print("Student record not found.")
        return
    print("What would you like to update?")
    print("1. Name")
    print("2. Grade")
    print("3. Attendance")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        records[roll]["name"] = input("Enter the new name: ").strip()
        print("Name updated successfully.")
    elif choice == '2':
        records[roll]["grade"] = input("Enter the new grade: ").strip()
        print("Grade updated successfully.")
    elif choice == '3':
        try:
            attendance = float(input("Enter the new attendance percentage: "))
            if attendance < 0 or attendance > 100:
                print("Attendance must be between 0 and 100.")
                return
            records[roll]["attendance"] = attendance
            print("Attendance updated successfully.")
        except ValueError:
            print("Invalid input! Attendance must be a number.")
    else:
        print("Invalid choice.")


def delete_student(records):
    """Delete a student record."""
    roll = input("Enter the Roll Number to delete: ").strip()
    if roll in records:
        del records[roll]
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")



student_records = {}

while True:
    print("\nStudent Record Keeper")
    print("1. Display All Students")
    print("2. Add a Student")
    print("3. Update a Student")
    print("4. Delete a Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_students(student_records)
    elif choice == '2':
        add_student(student_records)
    elif choice == '3':
        update_student(student_records)
    elif choice == '4':
        delete_student(student_records)
    elif choice == '5':
        print("Exiting Student Record Keeper. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

