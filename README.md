# School Enrollment Statistics

This Python code uses `NumPy` and `Matplotlib` libraries to import and visualize data related to the enrollment of high schools in the school district.

## Class
- `School`: A class that creates a school object with two attributes: `name` (string) representing the school's name, and `code` (integer) representing the school's code.

## Functions
- `print_all_stats()`: A method of the `School` class that prints the name and code of the school instance.

- `main()`: The main function that executes the program. It starts by printing a heading and then prompts the user for input of either a school name or code. It then verifies the user's input and prints the enrollment statistics for the selected school.

## Data Import
The code imports three CSV files, `SchoolData_2018-2019.csv`, `SchoolData_2019-2020.csv`, and `SchoolData_2020-2021.csv`, which contain the enrollment data for each school in the district for the corresponding year. The data is loaded into three `NumPy` arrays: `School_data_2019`, `School_data_2020`, and `School_data_2021`.

## Data Visualization
The program does not contain any data visualization, but the imported `Matplotlib` library could be used to create visualizations of the enrollment data.

# Author
Oluwafisayo Adabs - fisayoadabs
