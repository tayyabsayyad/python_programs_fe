def triangle_pattern(rows):
    """
    Print a right-angled triangle pattern with the given number of rows.

    Parameters:
        rows (int): The number of rows in the triangle.
    """
    for i in range(1, rows + 1):  # Loop from 1 to rows (inclusive)
        print("*" * i)  # Print '*' repeated i times



print("Triangle Pattern Generator")
try:
    rows = int(input("Enter the number of rows for the triangle pattern: "))
    if rows <= 0:
        print("Please enter a positive integer for the number of rows.")
    else:
        triangle_pattern(rows)
except ValueError:
    print("Invalid input! Please enter an integer value.")



'''
Sample Output :
Triangle Pattern Generator
Enter the number of rows for the triangle pattern: 10
*
**
***
****
*****
******
*******
********
*********
**********
'''