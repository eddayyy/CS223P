# Author Name: Eduardo NUnez
# Author email: eduardonunez@csu.fullerton.edu
# File Purpose: Calls the functions in contacts.py to apply them to the overall program. This file specifically
# makes sure that the user is introduced then prompted with their inputs 

from contacts import *

contact_list = []

print("      *** TUFFY TITAN CONTACT MAIN MENU\n1. Print list\n2. Add contact\n3. Modify contact\n4. Delete contact\n5. Exit the program")
while True:
     x = input("\nEnter menu choice: ")
     if x == "1":
          print_list(contact_list)
     elif x == '2':
          y = add_contact(contact_list)
     elif x == '3':
          modify_contact(contact_list)
     elif x == '4': 
          delete_contact(contact_list)
     elif x == '5':
          exit_program()
     else:    
          print("Invalid input. Feel free to run the program again. Good-Bye!")   
          quit()
