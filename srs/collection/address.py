class address():
    def __init__(self, name, number):
        self.__street = name
        self.__number = number
        
    def __str__(self):
        return self.__street + " street, nº" + int(self.__number)
    
    @property
    def street(self):
        return self.__street
    
    @property
    def number(self):
        return self.__number
