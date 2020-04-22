from address import address

class Packet():
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

        
    def number(self):
        s = str(self.__number1) + "-" + str(self.__number2) + "-" + str(self.__number3) + "-" + str(self.__number4)
        return s
    
    def add_error(self):
        self.__error = self.__error + 1
    
    @property
    def post_code(self):
        return self.__post_code
    
    @property
    def error(self):
        return self.__error
    
    
    
    
