from DoublyLinkedList import DList

class DSMember():
    """
    Atributes:
        identifier: Stores an identifier must have the following format: RXXXXXX where X can be any digit
        name: Stores the name
        surname: "" "" surname
        status: Stores whether the member is 'active' or 'inactive'
        __zones: (Dlist) Contains the zones the member has assignated
        __packets: (DList) Contains the list of packets to be delivered
    Methods:
        assign_zone(self, zones)
        assign_packet(self, packet)
        deliver_packet(self)
    """
    def __init__(self, ident, name, surname, status):
        if isinstance(ident, int) and len(str(ident)) <= 6:
            ceros_extra = 6 - len(str(ident))
            ceros = ''
            for _ in range (ceros_extra):
                ceros += '0'
            self.__identifier = "R" + ceros +str(ident)
        else:
            print("Error - identifier must follow the structure XXXXXX, with X being a number")
        self.__name = name
        self.__surname = surname
        self.__status = status
        self.__zones = DList()
        self.__packets = DList()
        
    def assing_zone(self, zones):
        if isinstance(zones, int):
            self.__zones.addLast(zones)
        else:
            print("Error - postal code must be a number")
            
    def assign_packet(self, packet):
        self.__packets.addLast(packet)
        
    def deliver_packet(self):
        return self.__packets.removeFirst()

    @property
    def identifier(self):
        return self.__identifier
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    def fullname(self):
        s = self.__surname + " "  + self.__name 
        return s
    
    @property
    def status(self):
        return self.__status
    
    @property
    def zones(self):
        return self.__zones
    
    def packetSize(self):
        return self.__packets.size()
