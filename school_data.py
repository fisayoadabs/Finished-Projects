# school_data.py
# OLUWAFISAYO ADABS 30141541, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays
School_data_2019 = np.genfromtxt("SchoolData_2018-2019.csv", delimiter= ",", skip_header= True) #Imports 2018-2019 data without commas
School_data_2020 = np.genfromtxt("SchoolData_2019-2020.csv", delimiter= ",", skip_header= True) #Imports 2019-2020 data without commas
School_data_2021 = np.genfromtxt("SchoolData_2020-2021.csv", delimiter= ",", skip_header= True) #Imports 2020-2021 data without commas

school_code = ['1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', '9825', '9826', '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858', '9860', '9865'] #Lists of school code
school_names = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School', 'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 'Ernest Manning High School', 'William Aberhart High School', 'National Sport School', 'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School', 'Jack James High School', 'Sir Winston Churchill High School', 'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School'] #List of school names
dict_code_names = dict(zip(school_code, school_names)) # Dictionary for school codes to school names
dict_names_code = dict(zip(school_names, school_code)) # Dictionary for school names to school codes

dict_code_index = dict(zip(school_code,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Dictionary for school codes to and index number 

# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array data for 2020-2021:\n', School_data_2021)
    print('Array data for 2019-2020:\n', School_data_2020)
    print('Array data for 2018-2019:\n', School_data_2019)
    # Add request for user input here    
    while True: # Loop program to ensure user inputs correct values as stated if not it loops until the correct value has been inputed
        request_code = input('Please enter a highschool name or the school code: ') # Request for user input
        request_code = request_code.strip() # Removes white spaces from the beginning and the end of the string(cause no space is to be included)
        if request_code in dict_code_names: # If statement to ensure if the users inputed school code is in the dictionary
            given_code = request_code # Variable that stores the code
            given_name = dict_code_names[request_code] # Variable that stores the school name from the user's inputed school code
        
            if given_code in dict_code_index: # If statement that checks if the school code is in another dictionary in order to print out the correct array row
                index_num = dict_code_index[given_code] # Variable that stores the index number from the user's inputed school code
            break # Terminates loop
        
        elif request_code in dict_names_code: # Elif statement to ensure if the users input a school name it is in the dictionary
            given_code = dict_names_code[request_code] # Variable that stores the user's school code from the user's inputed school name 
            given_name = request_code #Variable that stores the school name 

            if given_code in dict_code_index: # If statement that checks if the code is in another dictionary in order to print out the correct array row
                index_num = dict_code_index[given_code] # Variable that stores the index number from the user's inputed school code
            break # Terminates loop
        
        else: # Else statement that informs the user that the inputed value is incorrect and allows the user to retry
            print('You must enter a valid school name or code')
            True
    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    level = School(given_name, given_code) #Calls the class object
    level.print_all_stats() # Prints school name and code based on function in the class
    # Add data processing and plotting here
    grade_ten =  (School_data_2019[index_num, 1] + School_data_2020[index_num, 1] + School_data_2021[index_num, 1])//3 # Mean value calculation for grade 10 of each year for the specific school
    grade_eleven =  (School_data_2019[index_num, 2] + School_data_2020[index_num, 2] + School_data_2021[index_num, 2])//3 # Mean value calculation for grade 10 of each year for the specific school
    grade_twelve =  (School_data_2019[index_num, 3] + School_data_2020[index_num, 3] + School_data_2021[index_num, 3])//3 # Mean value calculation for grade 10 of each year for the specific school
    total_graduate = (School_data_2019[index_num, 3] + School_data_2020[index_num, 3] + School_data_2021[index_num, 3]) # Calculations of total graduates in the past three years
    print(f'Mean enrollment for Grade 10: {grade_ten:.0f}') # Prints out mean value for grade 10 with no decimal places
    print(f'Mean enrollment for Grade 11: {grade_eleven:.0f}') # Prints out mean value for grade 11 with no decimal places
    print(f'Mean enrollment for Grade 12: {grade_twelve:.0f}') # Prints out mean value for grade 12 with no decimal places
    print(f'Total number of students who graduated in the last three years: {total_graduate:.0f}') # Prints out total graduates students no decimal places
    
    years = [10, 11, 12] # Created grades list for x values
    student_num_2021 = [School_data_2021[index_num, 1], School_data_2021[index_num, 2], School_data_2021[index_num, 3]] # List for the students in the 2021 year for grades 11 10 and 12 for the desired school
    student_num_2020 = [School_data_2020[index_num, 1], School_data_2020[index_num, 2], School_data_2020[index_num, 3]] # List for the students in the 2020 year for grades 11 10 and 12 for the desired school
    student_num_2019 = [School_data_2019[index_num, 1], School_data_2019[index_num, 2], School_data_2019[index_num, 3]] # List for the students in the 2019 year for grades 11 10 and 12 for the desired school
    
    plt.scatter(x = years, y = student_num_2021, c = 'blue', label = '2021 Enrollment') # Plots point for total enrollment of students in grade 10 in 2020-2021 year with the colour blue and labels the colour blue as 2021 Enrollment
    plt.scatter(x = years, y = student_num_2020, c = 'green', label = '2020 Enrollment') # Plots point for total enrollment of students in grade 10 in 2019-2020 year with the colour green and labels the colour green as 2020 Enrollment
    plt.scatter(x = years, y = student_num_2019, c = 'red', label = '2019 Enrollment') # Plots point for total enrollment of students in grade 10 in 2018-2019 year with the colour red and labels the colour red as 2019 Enrollment
    plt.xticks(years) # Format's the scale of the x-axis to only show the three intergers in the list 
    
    plt.xlabel('Grade Level') # Labels the x-axis
    plt.ylabel('Number of Students') # Labels rhe y-axis
    plt.title('Grade Enrollment by Year') #Labels the graphs
    plt.legend(shadow = True) # Shows the lengend and shows a shadow of the lengend box
    
    #BONUS
    year = [2019, 2020, 2021] # Created years Lists for x values
    enrollment = [School_data_2019[index_num, 1], School_data_2020[index_num, 1], School_data_2021[index_num, 1]] # List for the students enrolled in grade 10 for 2019, 2020 and 2021 year for the desired school
    enrollment_one = [School_data_2019[index_num, 2], School_data_2020[index_num, 2], School_data_2021[index_num, 2]] # List for the students enrolled in grade 11 for 2019, 2020 and 2021 year for the desired school
    enrollment_two = [School_data_2019[index_num, 3], School_data_2020[index_num, 3], School_data_2021[index_num, 3]] # List for the students enrolled in grade 12 for 2019, 2020 and 2021 year for the desired school
    
    fig, sub = plt.subplots(3) # Figure command that creates three subplot graphs that are vertically stacked 
    fig.suptitle('Enrollment by Grade') # Title for the entire figure of the three subplots
    sub[0].plot(year, enrollment, linestyle = 'dashed', c = 'yellow', label = 'Grade 10') # PLots first subplot graph for the grade 10 enrollment with dashed line and the colour yellow and labels this line 'grade 10'
    sub[1].plot(year, enrollment_one, linestyle = 'dashed', c = 'magenta', label = 'Grade 11') # PLots second subplot graph for the grade 11 enrollment with dashed line and the colour magenta and labels this line 'grade 11'
    sub[2].plot(year, enrollment_two, linestyle = 'dashed', c = 'cyan', label = 'Grade 12') # PLots third subplot graph for the grade 12 enrollment with dashed line and the colour cyan and labels this line 'grade 12'
    plt.xlabel('Enrollment Year') # Labels x axis of the last sublpot graph (since it was meant for the plot and not a specific subplot it goes and the last subplot graphed)
    sub[0].set_ylabel('Number of Students') # Labels the y axis of the first subplot graph
    sub[1].set_ylabel('Number of Students') # Labels the y axis of the second subplot graph
    sub[2].set_ylabel('Number of Students') # Labels the y axis of the third subplot graph
    sub[0].legend(shadow = True) # Shows the lengend on the first subplot graph and shows a shadow of the lengend box
    sub[1].legend(shadow = True) # Shows the lengend on the second subplot graph and shows a shadow of the lengend box
    sub[2].legend(shadow = True) # Shows the lengend on the third subplot graph and shows a shadow of the lengend box
    plt.setp(sub, xticks = [2019, 2020, 2021] ) # Sets all the subplot graph x axis scale to be only those three intergers 
    
    plt.show() # Shows the graph


# Do not modify the code below
if __name__ == '__main__':
    main()

