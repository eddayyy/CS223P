# Author Name: Eduardo NUnez
# Author email: eduardonunez@csu.fullerton.edu
# File Purpose: Calls the functions in contacts.py to apply them to the overall program. This file specifically
# makes sure that the user is introduced then prompted with their inputs 

from contacts import *

contact_list = []

print("      *** TUFFY TITAN CONTACT MAIN MENu\n1. Print list\n2. Add contact\n3. Modify contact\n4. Delete contact\n5. Sort list by first name\n6. Sort list by last name\n7. Exit the program")
while True:
     x = input("\nEnter menu choice: ")
     if x == "1":
          print_list(contact_list)
     elif x == '2':
          z = input("\nEnter the first name: ")
          y = input("\nEnter the last name: ")
          add_contact(contact_list, first_name=z, last_name=y)
     elif x == '3':
          input_string = input("Enter the index number: ")
          i = int(input_string)
          z = input("Enter first name: ") 
          y = input("Enter last name: ")          
          modify_contact(contact_list,first_name = z, last_name=y, index = i )
     elif x == '4': 
          input_string = input("Enter the index number: ")
          i = int(input_string)         
          delete_contact(contact_list, index = i)
     elif x == "5":
          sort_contacts(contact_list, column = 0)
     elif x == "6":
          sort_contacts(contact_list, column = 1)
     elif x == '7':
          exit_program()
     else:    
          print("Invalid input")
          exit_program()
         