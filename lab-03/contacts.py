# Author Name: Eduardo NUnez
# Author email: eduardonunez@csu.fullerton.edu
# File Purpose: This file defines multiple functions that provide support of the overall program.
# Functions have doc strings that elaborate on the purpose and overall method. 

def print_list(contact_list):
    ''' This functions prints out our contacts list. '''
    print("\n================== CONTACT LIST ==================\n", "Index   First Name            Last Name\n", "======  ====================  ====================")
    for contact in contact_list:
        print(f'{contact_list.index(contact)}\t {contact[0]}\t\t\t{contact[1]}')



def add_contact(contact_list,*, first_name = "", last_name = ""):
    ''' This function allows the user to add a contact to contact_list.''' 
    contact_list.append([first_name, last_name])
    return contact_list



def modify_contact(contact_list, first_name, last_name, index):
    ''' This function allows the user to modify an element in contact_list.'''
    if index < len(contact_list):
        contact_list.pop(index)
        contact_list.insert(index, [first_name, last_name])
        # contact_list[modified_contact] = [x, y]
        return True

    else:
        print("Invalid index number.")
        return False




def delete_contact(contact_list, index = 1):
    ''' This function allows the user to delete a contact from conact_list.'''
    if index <= len(contact_list):
        contact_list.pop(index)
        return True
    else:
        print("Invalid index number.")
        return False



def sort_contacts(contact_list, column = 0):
    if column == 0:
        contact_list.sort(key=lambda x: x[0])
        return contact_list
    elif column == 1:
        contact_list.sort(key=lambda x: x[1])
        return contact_list        


def exit_program():
    print("You have chosen to exit the program. Good-Bye!")
    quit()