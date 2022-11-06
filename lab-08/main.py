# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

from people import Person
from people import Faculty
from people import Student

faculty_list = []
student_list = []

while True:
    x = int(input(f" *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n\n1. Add faculty\n2. Print faculty\n3. Add student\n4. Print student\n5. Exit the program\n"))
    
    if x == 1:
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        department = input("Enter department: ")
        faculty_object = Faculty(first_name, last_name, department)
        faculty_list.append(faculty_object)
      
    if x == 2:
        for item in range(len(faculty_list)):
            print(faculty_list[item])    
            
    if x == 3:
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        classyear = input("Enter class year: ")
        major = input("Enter major: ")
        faculty_advisor = input('Enter Faculty Advisor:' )
        
        
    if x == 4:
        for item in range(len(student_list)):
            print(student_list[item])
    if x == 5:
        exit()
        