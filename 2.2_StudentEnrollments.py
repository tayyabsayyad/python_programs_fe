def display_set(student_set, message):
    """Display the contents of a set with a message."""
    if student_set:
        print(f"\n{message}:")
        print(", ".join(student_set))
    else:
        print(f"\n{message}: No students in this set.")


# Initialize sets for enrollments
cet_students = set()
jee_students = set()
neet_students = set()

while True:
    print("\nStudent Enrollment Manager")
    print("1. Add Student to CET")
    print("2. Add Student to JEE")
    print("3. Add Student to NEET")
    print("4. Display Students in CET, JEE, or NEET")
    print("5. Perform Union (Students in Any Exam)")
    print("6. Perform Intersection (Students in All Exams)")
    print("7. Perform Difference (Students in CET but Not in Others)")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        name = input("Enter the name of the student to add to CET: ").strip()
        cet_students.add(name)
        print(f"Student {name} added to CET.")
    elif choice == '2':
        name = input("Enter the name of the student to add to JEE: ").strip()
        jee_students.add(name)
        print(f"Student {name} added to JEE.")
    elif choice == '3':
        name = input("Enter the name of the student to add to NEET: ").strip()
        neet_students.add(name)
        print(f"Student {name} added to NEET.")
    elif choice == '4':
        print("\nSelect which group to display:")
        print("1. CET")
        print("2. JEE")
        print("3. NEET")
        group_choice = input("Enter your choice (1-3): ")
        if group_choice == '1':
            display_set(cet_students, "CET Students")
        elif group_choice == '2':
            display_set(jee_students, "JEE Students")
        elif group_choice == '3':
            display_set(neet_students, "NEET Students")
        else:
            print("Invalid choice.")
    elif choice == '5':
        union_set = cet_students | jee_students | neet_students
        display_set(union_set, "Students Enrolled in Any Exam")
    elif choice == '6':
        intersection_set = cet_students & jee_students & neet_students
        display_set(intersection_set, "Students Enrolled in All Exams")
    elif choice == '7':
        difference_set = cet_students - jee_students - neet_students
        display_set(difference_set, "Students in CET but Not in JEE or NEET")
    elif choice == '8':
        print("Exiting the Student Enrollment Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
