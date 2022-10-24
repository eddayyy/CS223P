# Author: Eduardo Nunez
# Author Email: eduardonunez@csu.fullerton.edu

from contacts import *

contact_dictionary = {}

print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Find contact\n6. Exit the program")
while True:
   x = input("\nEnter menu choice: ")
   if x == "1":
      add_contact(contact_dictionary, id = input("\nEnter the phone number: "), first_name = input("\nEnter the first name: "), last_name = input("\nEnter the last name: "))
   elif x == '2':
      modify_contact(contact_dictionary,id = input("\nEnter phone number: "), first_name = input("\nEnter first name: "), last_name = input("\nEnter last name: "))
   elif x == '3':
      delete_contact( contact_dictionary, id = input("Enter phone number: ") )
   elif x == '4':
      print_contacts(contact_dictionary)
   elif x == '5':
      f = input("Enter search string: ")
      find_contact(contact_dictionary, find = f )
   elif x == '6':
      quit()