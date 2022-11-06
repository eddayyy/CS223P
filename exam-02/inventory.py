# Author name: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu
# Date: 11/01/2022 
# inventory dictionary:
#               inventory_dict = {BCnnn : self.item_list}
# BCnnn -> "BC"nnn as ints""
# item list:    element 0 : description as a string
#               element 1 : quantity in inventory as int


import json

class Inventory:
    def __init__(self, /, *, filename):
       self.data = {}
       self.filename = filename
       try:
           with open( filename, 'r' ) as file:
               self.data = json.load( file )
       except FileNotFoundError:
           return None
              
    def add_item( self, /, *, barcode, description ):
        if type( barcode ) == int:
            return 109
        if type( barcode ) == str:
            if not len( barcode ) == 6 or not barcode[:2] == "BC":
                return 109
            if not barcode[2:6].isdigit():
                return 109
        
        if barcode in self.data:
            return 101
        
        self.data[ barcode ] = [ description, 0 ]

        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except FileNotFoundError:
            return None
        
        return 100
    

        
    def modify_description( self, /, *, barcode, description ):
        if barcode not in self.data.keys():
            return 102
        desc, qty = self.data[ barcode ]
        self.data[ barcode ] = [ description, qty ]
        try:
            with open( self.filename, 'w' ) as file:
                json.dump( self.data, file )
        except FileNotFoundError:
              return None
        return 100
    
    def add_qty(self, /, *, barcode, qty):
        x = qty
        if barcode not in self.data:
            return 102
        
        if type(x) != int:
            return 108
        
        desc, t_qty = self.data[barcode]
        self.data[barcode] = (desc, t_qty + qty)
        try:
            
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
                
        except FileNotFoundError:
            return None
        
        return 100
    
    def remove_qty(self, /, *, barcode, qty):
        
        if barcode not in self.data:
            return 102
        
        if type(qty) != int:
            return 108
        
        desc, t_qty = self.data[barcode]
        
        if qty > t_qty:
            return 103 
        
        self.data[barcode] = [desc, t_qty - qty]
        
        try: 
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except FileNotFoundError:
            return None
        return 100
        
        
    def get_inventory(self, /):
        report = str()
        for barcode, item_list in self.data.items():
            report = report + f'{barcode:8}{item_list[0]:20}{item_list[1]:5}\n'
        return report     
        