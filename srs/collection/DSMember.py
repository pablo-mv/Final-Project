import sys
sys.path.append('../../')
from srs.collection.DoublyLinkedList import DList

class DSMember():
    """
    Atributes:
        identifier: Stores an identifier must have the following format: RXXXXXX where X can be any digit
        name: Stores the name
        surname: "" "" surname
        status: Stores whether the member is 'active' or 'inactive'
        __zones: (Dlist) Contains the zones the member has assignated
        __packets: (DList) Contains the list of packets to be delivered
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
    
    def __str__(self):
        """
        Gives the data of the DSMember for printing
        Worse case: O(1)
        Best case: O(1)
        """
        s = 'Id: ' + self.__identifier + '\n'
        s += 'Name: ' + self.__name + '\n'
        s += 'Surname: ' + self.__surname +'\n'
        s += 'Status: ' + self.__status  + '\n'
        s += 'Zones: ' + str(self.__zones) + '\n'
        s += 'Packets: ' + str(self.__packets)[1:-1] + '\n'
        return s
        
       
    def assing_zone(self, zones):
        """
        Stores a postal code into a DList
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        if isinstance(zones, int):
            self.__zones.addLast(zones)
            
        else:
            print("Error - postal code must be a number")
            
    def assign_packet(self, packet):
        """
        Stores a package into a DList
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        self.__packets.addLast(packet)
        
    def deliver_packet(self):
        """
        Simulates the delivery of a packet
        Complexity Worse Case: O(1)
        Complexity Best Case: O(1)
        """
        return self.__packets.removeFirst()

    def fullname(self):
        """
        Returns the fullname of a DSMember (surname name)
        Complexity Worse Case: O(1)
        Complexity Best Case: O(1)
        """
        s = self.__surname + " "  + self.__name 
        return s
    
    def packetSize(self):
        """
        Returns the number of packages the current DSMember has.
        Complexity Worse Case: O(1)
        Complexity Best Case: O(1)
        """
        return self.__packets.size
    
    def getPacket(self, idx):
        """
        Returns a package into a DList with the index idx
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        return self.__packets.getAt(idx)
    
    @property
    def identifier(self):
        return self.__identifier
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, newStatus):
        self.__status = newStatus
    
    @property
    def zones(self):
        return self.__zones
    

