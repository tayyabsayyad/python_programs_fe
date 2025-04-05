def calculate_gross_salary(basic_salary):

    # Allowances as percentages of basic salary
    dearness_allowance = 0.70 * basic_salary
    travel_allowance = 0.30 * basic_salary
    house_rent_allowance = 0.10 * basic_salary

    # Calculate gross salary
    gross_salary = basic_salary + dearness_allowance + travel_allowance + house_rent_allowance

    return gross_salary, dearness_allowance, travel_allowance, house_rent_allowance


print("---> Gross Salary Calculator <---")
try:
    # Input basic salary
    basic_salary = float(input("Enter the Basic Salary (BS) of the employee: "))

    if basic_salary < 0:
        print("Basic Salary cannot be negative. Please enter a valid amount.")
        exit(0) 
    # Calculate gross salary and allowances
    gross_salary, da, ta, hra = calculate_gross_salary(basic_salary)

    # Display the result
    print("\nSalary Breakdown:")
    print(f"Basic Salary (BS): ₹{basic_salary:.2f}")
    print(f"Dearness Allowance (DA - 70% of BS): ₹{da:.2f}")
    print(f"Travel Allowance (TA - 30% of BS): ₹{ta:.2f}")
    print(f"House Rent Allowance (HRA - 10% of BS): ₹{hra:.2f}")
    print(f"Gross Salary: ₹{gross_salary:.2f}")

except ValueError:
    print("Invalid input! Please enter a numeric value for the Basic Salary.")
