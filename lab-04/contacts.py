# Author: Eduardo Nunez
# Author Email: eduardonunez@csu.fullerton.edu


def add_contact(contact_dictionary,*, id, first_name, last_name):
    ''' This function allows addition of key-value pairs in our dictionary.'''
    if id in contact_dictionary:
        print("Key exists")
        return "error"
    else:
        contact_dictionary[id] = [first_name, last_name]
        return contact_dictionary


def modify_contact(contact_dictionary, *, id, first_name, last_name):
    '''This function allows the modification of contacts in our dictionary.'''
    if id not in contact_dictionary:
        print("\nPhone number does not exist.\n")
        return "error"
    elif id in contact_dictionary:
        contact_dictionary[id] = [first_name, last_name]
        print("Modified: ", first_name, " ", last_name, ".\n")
        return contact_dictionary


def delete_contact(contact_dictionary, *, id):
    '''This function allows the destruction of contacts in our dictionary.'''
    if id in contact_dictionary:
        print("Deleted ", contact_dictionary[id], " \n")
        del contact_dictionary[id]
        return contact_dictionary
    elif id not in contact_dictionary:
        print("\nInvalid phone number.\n")
        return "error"

def print_contacts(contact_dictionary):
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Find contact\n6. Exit the program\n")
    print("==================== CONTACT LIST ====================")
    print("Last Name             First Name            Phone")
    print("====================  ====================  ==========")    
    sort_contacts(contact_dictionary)
    # for key, value in contact_dictionary.items():
    #     print(value[1],"\t\t\t", value[0],"\t\t", key)

def sort_contacts(contact_dictionary):
    ''' This function sorts the contacts in our dictionary. '''

    # dictionary has no sort() function, so convert dictionary to list of tuples
    lt1 = list(contact_dictionary.items())

    # define sort for dictionary left value, which is now the left list element of the right tuple
    def mySortDicValueRightThenLeft(inner_element):
        return (inner_element[1][1].lower(),inner_element[1][0].lower()) # pack the right primary then left secondary in a tuple itself
    print_found()
    # sort it
    lt1.sort(key= mySortDicValueRightThenLeft)
    for left_tuple, right_tuple in lt1:
        print(f'{right_tuple[1]:10}{right_tuple[0]:10}{str(left_tuple):5}')

    # convert back to dictionary
    d1 = dict(lt1)
    return d1

def find_contact(contact_dictionary, *, find):
    result = dict()
    if find.isnumeric():
        if int(find) in contact_dictionary:
            result[int(find)] = contact_dictionary[int(find)]
    else: 
        for key, [fname, lname] in contact_dictionary.items():
            if fname.lower() == find.lower() or lname.lower() == find.lower():
                result[key] = [fname, lname]
    return sort_contacts(result)                 



def print_found():
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n1. Add contact\n2. Modify contact\n3. Delete contact\n4. Print contact list\n5. Find contact\n6. Exit the program\n")
    print("==================== FOUND CONTACT(S) ====================")
    print("Last Name             First Name            Phone")
    print("====================  ====================  ==========")    
