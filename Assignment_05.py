# ------------------------------------------------------------------------------------------ #
# Title: Assignment05 - Working With Dictionaries And JSON Files
# Desc: Course Registration Program using dictionaries and exception handling
# Change Log: (Who, When, What)
#   Jeff Hart,05/24/2025,Created Script for Assignment05
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
------------------------------------------
'''

FILE_NAME: str = "Enrollments.json"

# Define the program's variables
student_first_name: str = ''  # Holds the first name of a student entered by the user
student_last_name: str = ''   # Holds the last name of a student entered by the user
course_name: str = ''         # Holds the course name entered by the user
file = None                   # File object for reading/writing
menu_choice: str = ''         # Hold the choice made by the user
student_data: dict = {}       # One row of student data
students: list = []           # A list of student data dictionaries

# When the program starts, read the file data into the students list
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    print("Successfully loaded existing data from {}.".format(FILE_NAME))
except FileNotFoundError as e:
    print("File '{}' not found. Starting with empty student list.".format(FILE_NAME))
    print("The file will be created when you save data.")
    students = []  # Start with empty list if file doesn't exist
    
    # Create the file with empty list so it exists for next time
    try:
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        print("Created new empty {} file.".format(FILE_NAME))
    except Exception as create_error:
        print("Warning: Could not create {}. File will be created when you save data.".format(FILE_NAME))
        
except json.JSONDecodeError as e:
    print("Error: {} contains invalid JSON format!".format(FILE_NAME))
    print("Starting with empty list. Please check your JSON file syntax.")
    print("-- Technical Error Message --")
    print("Error: {}".format(e))
    students = []
except Exception as e:
    print("There was a non-specific error reading the file!")
    print("-- Technical Error Message --")
    print("Error: {}, Type: {}".format(e, type(e)))
    students = []  # Start with empty list if other error occurs
finally:
    if file and not file.closed:
        file.close()

# Main program loop
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer

    if menu_choice == "1":
        # Register a Student for a Course
        try:
            # Input the student's first name with error handling
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letters.")
            
            # Input the student's last name with error handling  
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letters.")
            
            # Input the course name
            course_name = input("What course would you like to register for? ")
            if not course_name.strip():
                raise ValueError("Course name cannot be empty.")
            
            # Create student data dictionary and add to students list
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            
            print("You have registered {} {} for {}.".format(
                student_first_name, student_last_name, course_name))
            
        except ValueError as e:
            print("Input Error: {}".format(e))
            print("-- Technical Error Message --")
            print("Error Type: {}".format(type(e)))
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print("Error: {}, Type: {}".format(e, type(e)))
        continue

    elif menu_choice == "2":
        # Show current data
        print("-" * 50)
        print("The current data is:")
        
        if not students:
            print("No students are currently registered.")
        else:
            # Display formatted data
            for student in students:
                print("Student {} {} is registered for {}.".format(
                    student["FirstName"], student["LastName"], student["CourseName"]))
            
            print()
            print("Raw data (comma-separated values):")
            # Display comma-separated values for each row
            for student in students:
                print("{},{},{}".format(
                    student["FirstName"], student["LastName"], student["CourseName"]))
        
        print("-" * 50)
        continue

    elif menu_choice == "3":
        # Save data to a file
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            
            print("Data saved to {}!".format(FILE_NAME))
            print("Current data written to file:")
            
            # Display what was written to the file
            for student in students:
                print("Student {} {} is registered for {}.".format(
                    student["FirstName"], student["LastName"], student["CourseName"]))
                    
        except Exception as e:
            print("Error saving data to file!")
            print("-- Technical Error Message --")
            print("Error: {}, Type: {}".format(e, type(e)))
        finally:
            if file and not file.closed:
                file.close()
        continue

    elif menu_choice == "4":
        # Exit the program
        print("Thank you for using the Course Registration Program!")
        break  # Exit the while loop

    else:
        print("Invalid menu choice. Please select 1, 2, 3, or 4.")
        continue
