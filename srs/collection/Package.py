import sys
import os

sys.path.append(os.getcwd())

from srs.collection.address import address

class Packet():
    """
    Creates a package with an identifier based on XXX-XXXXXX-XXXXXX, with X being a digit
    Atributes
    post_code: Contains the postal code
    error: Contains the errors
    __number1, __number2, __number3: Contain the numbers of the identifier
    __adress: Constains the object type addressz
    Methods
    number: returns the identifier of the package
    add_error: 
    
    """
    
    def __init__(self, number1, number2, number3, add_name, add_number, post_code, number_errors = 0):
        if isinstance(number1, int) and len(str(number1)) == 3:
            self.__number1 = number1
        else:
            print("Error - number must follow the structure XXX-XXXXXX-XXXXXX")
            
        if isinstance(number2, int) and len(str(number2)) == 6:
            self.__number2 = number2
        else:
            print("Error - number must follow the structure XXX-XXXXXX-XXXXXX")
            
        if isinstance(number3, int) and len(str(number3)) == 6:
            self.__number3 = number3
        else:
            print("Error - number must follow the structure XXX-XXXXXX-XXXXXX")
            
            
        if isinstance(post_code, int):
            self.__post_code = post_code
        else:
            print("Error - postal codemust be a number")
            
        self.__address = address(add_name,add_number)
        self.__error = number_errors

    def __str__(self):
        s = '\nId: ' + str(self.__number1) + "-" + str(self.__number2) + "-" + str(self.__number3) + '\n'
        s += 'Directioin: ' + str(self.__address) +', '+ str(self.post_code) +'\n' 
        s += 'Errors: ' + str(self.error) 
        return s
        
    def number(self):
        """
        Returns the id of the packet
        Best and worst case: O(1)
        """
        s = str(self.__number1) + "-" + str(self.__number2) + "-" + str(self.__number3)
        return s
    
    def add_error(self):
        """
        Increases 1 to the number of errors
        Best and worst case: O(1)
        """
        self.__error = self.__error + 1
    
    @property
    def post_code(self):
        return self.__post_code
    
    @property
    def error(self):
        return self.__error
    
    
    
    
    
