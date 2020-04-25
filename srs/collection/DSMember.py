import sys
sys.path.append('../')
from srs.collection.DoublyLinkedList import DList

class DSMember():
  
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
        s = 'Id: ' + self.__identifier + '\n'
        s += 'Name: ' + self.__name + '\n'
        s += 'Surname: ' + self.__surname +'\n'
        s += 'Status: ' + self.__status  + '\n'
        s += 'Zones: ' + str(self.__zones) + '\n'
        s += 'Packets: ' + str(self.__packets)[1:-1] + '\n'
        return s
        
       
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
    @status.setter
    def status(self, newStatus):
        self.__status = newStatus
    
    @property
    def zones(self):
        return self.__zones
    
    def packetSize(self):
        return self.__packets.size
    
    def getPacket(self, idx):
        return self.__packets.getAt(idx)
