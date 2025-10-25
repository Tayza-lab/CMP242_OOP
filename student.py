# Please Tayza include comments on each block of your code explaining the reason behind it.
# Indicate the topic or new development that is introduced based on the topic covered 
# I will choose the best ideas & then we'll work together  
import email  # Importing the email module, though it seems not to be used in the current code snippet

# Class definition for the Students
class Students:
    # Class-level variable for the discount amount, shared across all instances
    discount_amt = 200  # This means each student will have a 200 discount associated by default

    # Constructor method to initialize the student instance
    def __init__(self, student_id, first_name, last_name, email):
        # Instance variables: The student ID, first and last names, and email address are stored for each student
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # Method to display basic student info (such as student ID and email)
    def display_info(self):
        # Returns a formatted string containing student ID and email
        return f"Student ID: {self.student_id}, Email: {self.email}"

    # Method to return the full name of the student (combines first and last names)
    def full_name(self):
        # Combines first and last name and returns the full name
        return f"{self.first_name} {self.last_name}"

# Creating instances (students) using the constructor
student1 = Students("K2023XXXX", "John", "Doe", "john.doe@example.com")  # Example student with ID, name, and email
k2023xxxx = Students("K2023YYYY", "Jane", "Smith", "jane.smith@example.com")  # Another student

# Calling the display_info method to print student information
print(student1.display_info())  # Displaying the info for student1
print(k2023xxxx.display_info())  # Displaying the info for k2023xxxx

# Calling the full_name method to print the full name of each student
print(student1.full_name())  # Printing full name for student1
print(k2023xxxx.full_name())  # Printing full name for k2023xxxx

