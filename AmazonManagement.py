from srs.collection.DSMembers import DSMembers
from srs.collection.DoublyLinkedList import DList
from srs.collection.DSMember import DSMember
from random import randint

class AmazonManagement():
    def __init__(self):
        self.__Delivered = DList()
        self.__Incidents = DList()
    
    def loadOrders(self):
        self.__Orders = DList()
        
    def loadDSMembers(self):
        self.__DSMembers = DSMembers()
        
    def showDSMember(self):
        self.__DSMembers.sortAlphabeticalSurname()
        for i in range(self.__DSMembers.size()):
            currentName = self.__DSMembers.getAt(i)
            print(currentName.fullname())
            
    def assignDistribution(self):
        for _ in range(self.__packets.size):
            current_packet = self.__packets.removeFirst
            con = False
            i = 1
            staff_free = self.__staff_list.head
            while not con and i <= self.__staff_list.size:
                current_staff = self.__staff_list.getAt(i)
                if current_staff.zones.contains(current_packet.post_code):
                    con = True
                    current_staff.assign_packet(current_packet)
                if current_staff.zones.size() < staff_free.zones.size():
                    staff_free = current_staff
                i = i + 1
            if not con:
                staff_free.assing_zone(current_packet.post_code)
                staff_free.assign_packet(current_packet)
                
    def deliverPackages(self,distributor):
        i = 0
        size = distributor.packetSize()
        while i < size:
            n = randint(0,100)
            if n < 90:
                currentPacket = distributor.packetSize()
                self.__Delivered.addLast(distributor.deliver_packet(currentPacket))
                i = i + 1
                print("The packet " + str(currentPacket.number()) + "has been delivered")
            else:
                currentPacket = distributor.packetSize()
                currentPacket.add_error()
                if currentPacket.error() < 3:
                    distributor.assign_packet(currentPacket)
                    print("The packet " + str(currentPacket.number()) + "is pending. It has " + str(currentPacket.error()) + " errors")
                else:
                    self.__Incidents.addLast(currentPacket)
                    print("The packet " + str(currentPacket.number()) + "has been removed due to continuous errors")
                
            
    def deliver(self):
        for i in range(self.__DSMembers.size):
            self.deliverPackages(self.__DSMembers.getAt(i))
            
    def removeDSmember(self,distributor):        
        if distributor.packetSize != 0:
            for _ in range(distributor.__packets.size):
                current_packet = distributor.__packets.removeFirst
                con = False
                i = 1
                while not con and i <= self.__staff_list.size:
                    current_staff = self.__staff_list.getAt(i)
                    if current_staff.zones.contains(current_packet.post_code):
                        con = True
                        current_staff.assign_packet(current_packet)
                    i = i + 1
                if not con:
                    self.__Incidents.addLast(currentPacket)
                    print("The packet " + str(currentPacket.number()) + "has been removed due to staff not being available")
                                
                
                    
        
        
