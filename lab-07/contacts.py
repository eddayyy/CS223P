# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

import json

def mySortFirstName(inside_element):
    return inside_element[0] # [0] picks left tuple

def mySortLastName(inside_element):
    return inside_element[1] # [1] picks right tuple

class Contacts:
            
    def __init__(self, filename):
        self.file_name = filename
        self.contact_dict = {}
        try:
            with open(filename, 'r') as f:
                x = json.load(f)
                self.contact_dict = x
        except FileNotFoundError:
            return {}
    
    def add_contact(self,*, id, first_name, last_name):
        phone_number = id
        if phone_number in self.contact_dict:
            return 'error'
        
        self.contact_dict.update({id:[first_name, last_name]})
        # sort dictionary 
        contact_list = list( self.contact_dict.items() )
        contact_list.sort( key = mySortFirstName )
        contact_list.sort( key = mySortLastName )
        self.contact_dict = dict(contact_list)
        
        with open(self.file_name, 'w') as f:
             x = json.dumps(self.contact_dict)
             f.write(x)
        added_contact = { id : [first_name, last_name]}
        return added_contact
        

    def modify_contact(self, /,*, id, first_name, last_name):   
        if id not in self.contact_dict:
            return 'error'
        modified_contact = {id : [first_name, last_name]}
        self.contact_dict.update(modified_contact)
        
        # sort dictionary 
        contact_list = list( self.contact_dict.items() )
        contact_list.sort( key = mySortFirstName )
        contact_list.sort( key = mySortLastName )
        self.contact_dict = dict( contact_list )
        
        with open( self.file_name, 'w' ) as f:
            y = json.dumps( self.contact_dict )
            f.write( y )
        return modified_contact
    
    def delete_contact( self, /,*, id ):
        if id not in self.contact_dict:
            return 'error'
        x = self.contact_dict[id]
        del self.contact_dict[id]
        with open(self.file_name, 'w') as f:
            y = json.dumps(self.contact_dict)
            f.write(y)
        return x 
    
    
