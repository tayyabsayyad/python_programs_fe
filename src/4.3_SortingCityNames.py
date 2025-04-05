def sort_city_names(input_file, output_file):
    """
    Read city names from a file, sort them alphabetically, and write them to another file.

    Parameters:
        input_file (str): The name of the file containing city names.
        output_file (str): The name of the file to write sorted city names.
    """
    try:
        # Read city names from the input file
        with open(input_file, 'r') as infile:
            city_names = infile.readlines()

        # Strip whitespace and sort city names alphabetically
        city_names = [city.strip() for city in city_names]
        city_names.sort()

        # Write the sorted city names to the output file
        with open(output_file, 'w') as outfile:
            for city in city_names:
                outfile.write(city + '\n')

        print(f"City names sorted alphabetically and written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


print("City Name Sorter")
input_file = input("Enter the input file name (with extension): ").strip()
output_file = input("Enter the output file name (with extension): ").strip()
sort_city_names(input_file, output_file)

