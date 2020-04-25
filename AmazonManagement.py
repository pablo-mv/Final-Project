import sys
sys.path.append('../')

from srs.collection.DSMembers import DSMembers
from srs.collection.DoublyLinkedList import DList
from srs.collection.Delivered import Delivered
from srs.collection.Incidents import Incidents
from random import randint


class AmazonManagement():
    def __init__(self):
        self.__Delivered = DList()
        self.__Incidents = DList()
        self.__Orders = DList()
        self.__DSMembers = DSMembers()
    
    def loadOrders(self, orders):
        for i in range(orders.size):
            self.__Orders.addLast(orders.removeFirst())
          
    def loadDSMembers(self, members):
        for i in range(members.size):
            self.__DSMembers.addLast(members.removeFirst())
                   
    def showDSMember(self):
        self.__DSMembers.sortAlphabeticalSurname()
        for i in range(self.__DSMembers.size):
            currentName = self.__DSMembers.getAt((i+1)%self.__DSMembers.size)
            print(currentName, end = '\n\n')
    @property
    def orders(self):
        return self.__Orders
    def assignDistribution(self): 
        for _ in range(self.__Orders.size): #__packets
            current_packet = self.__Orders.removeFirst()# __packets
            i = 1
            indx_member_size = [-1,999999] # Changes if we find a member active with space
            con = False
            n = self.__DSMembers.size
            while i <=n:
                current_staff = self.__DSMembers.removeFirst()
                if current_staff.zones.contains(current_packet.post_code) and current_staff.status == 'Active':
                    current_staff.assign_packet(current_packet)
                    con = True
 
                elif current_staff.zones.size < indx_member_size[1] and current_staff.status == 'Active':
                    indx_member_size = [i, current_staff.zones.size]
                    
                i += 1
                self.__DSMembers.addLast(current_staff)
                
            if indx_member_size[0] != -1 and not con:
                staff_free = self.__DSMembers.removeAt((indx_member_size[0]))
                staff_free.assing_zone(current_packet.post_code)
                staff_free.assign_packet(current_packet)
                self.__DSMembers.insertAt((indx_member_size[0]), staff_free)
                
            

                
    def deliverPackages(self,distributor): #Can not work with a distributor of the list alone. It requires deliver() in order to do so.
        i = 0
        size = distributor.packetSize()
        
        while i < size:
            currentPacket = distributor.deliver_packet()
            n = randint(0,1)
            if bool(n):
                self.__Delivered.addLast(Delivered(currentPacket.number(), distributor.identifier))
                i = i + 1
                print("The packet " + str(currentPacket.number()) + "has been delivered")
            else:
                currentPacket.add_error()
                if currentPacket.error< 3:
                    distributor.assign_packet(currentPacket)
                    print("The packet " + str(currentPacket.number()) + "is pending. It has " + str(currentPacket.error) + " errors")
                else:
                    self.__Incidents.addLast(Incidents(currentPacket.number(), distributor.identifier, 'Number of delivery attemps exceeded'))
                    print("The packet " + str(currentPacket.number()) + "has been removed due to continuous errors")
                    i+=1
        return distributor
        
            
    def deliver(self):
        for i in range(self.__DSMembers.size):
            member = self.__DSMembers.removeFirst()
            updated_member = self.deliverPackages(member)
            self.__DSMembers.addLast(updated_member)
            
    def removeDSMember(self,identifier):  
        distributor = self.__DSMembers.removeById(identifier)
        distributor.status = 'Inactive'
        if distributor.packetSize != 0:
            for _ in range(distributor.packetSize()):
                current_packet = distributor.deliver_packet()
                con = False
                i = 1
                while not con and i <= self.__DSMembers.size:
                    current_staff = self.__DSMembers.getAt(i)
                    if current_staff.zones.contains(current_packet.post_code):
                        con = True
                        current_staff.assign_packet(current_packet)
                    i += 1
                if not con:
                    self.__Incidents.addLast(Incidents(current_packet.number, '', 'Staff unavailable')) #currentPacket
                    print("The packet " + str(current_packet.number()) + "has been removed due to staff not being available") # currentPacket
        self.__DSMembers.addLast(distributor)                             
