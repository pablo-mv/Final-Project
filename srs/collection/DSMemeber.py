from DoublyLinkedList import DList

class DSMember():
    def __init__(self, ident, name, surname, status):
        if isinstance(ident, int) and len(str(ident)) == 6:
            self.__identifier = "R" + str(ident)
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
