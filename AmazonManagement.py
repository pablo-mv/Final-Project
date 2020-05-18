import sys
import os
sys.path.append(os.getcwd())

from srs.collection.DSMembers import DSMembers
from srs.collection.DoublyLinkedList import DList
from srs.collection.Delivered import Delivered
from srs.collection.Incidents import Incidents
from random import randint


class AmazonManagement():
    """
    Atributes:
        __Delivered: DList which stores Deliverd objects which contains the id of the package and of the deliverer
        __Incidents: DList which stores Incidents objects
        __Orders: Stores the packages which had not been assignated to a deliverer yet
        __DSMembers: DList which stores all the DSMember (The deliverers)
    """
    def __init__(self):
        self.__Delivered = DList()
        self.__Incidents = DList()
        self.__Orders = DList()
        self.__DSMembers = DSMembers()
    
    def loadOrders(self, orders):
        """
        Takes a DList of pakages and store them in an internal list
        Complexity Worse Case: O(n)
        Complexity Best Case: O(n)
        """
        for _ in range(orders.size):
            self.__Orders.addLast(orders.removeFirst())
          
    def loadDSMembers(self, members):
        """
        Takes a DList of DMember and store them in a DMembers list
        Complexity Worse Case: O(n)
        Complexity Best Case: O(n)
        """
        for _ in range(members.size):
            self.__DSMembers.addLast(*members.removeFirst())
                   
    def showDSMember(self):
        """
        First, orders alphabhetically by surname, then print the data of every
        DSMember
        Complexity Worse Case: O(n^2)
        Complexity Best Case: O(n^2)
        """
        self.__DSMembers.sortAlphabeticalSurname()  # n^2
        for i in range(self.__DSMembers.size):
            currentName = self.__DSMembers.getAt((i+1)%self.__DSMembers.size)
            print(currentName, end = '-----------------------------\n')

    def assignDistribution(self): 
        """
        Takes all the packages stored and assign them to all the delivery staff.
        
        Complexity Worse Case: O(n^3)
        Complexity Best Case: O(n^2)
        """
        for _ in range(self.__Orders.size):
            current_packet = self.__Orders.removeFirst()
            i = 0
            indx_member_size = [-1,999999]
            con = False
            n = self.__DSMembers.size
            while i <n:
                
                current_staff = self.__DSMembers.removeFirst()
                print(i)
                if current_staff.zones.contains(current_packet.post_code) and current_staff.status == 'Active':
                    current_staff.assign_packet(current_packet)
                    con = True
                    
                
                elif current_staff.zones.size < indx_member_size[1] and current_staff.status == 'Active':
                    
                    indx_member_size = [i, current_staff.zones.size]
                    
                i += 1
                self.__DSMembers.addLast(current_staff.identifier, current_staff.name, current_staff.surname, current_staff.status, current_staff.zones, current_staff.packets)
                
            if indx_member_size[0] != -1 and not con:  
 
                staff_free = self.__DSMembers.removeAt((indx_member_size[0]))
                staff_free.assing_zone(current_packet.post_code)
                staff_free.assign_packet(current_packet)
                self.__DSMembers.insertAt((indx_member_size[0]), staff_free.identifier, staff_free.name, staff_free.surname, staff_free.status, staff_free.zones, staff_free.packets)
                
            

                
    def deliverPackages(self,distributor):
        """
        Simulates the delivery of a packet. It has 1/2 of probability of being 
        delivered and 1/2 of not. The attept is done 3 times. If it fails. It is 
        stored as an Incidents. If it success, it is stored as a Delivered.
        It takes a DSMember, but in order to make it work with all the list of 
        members we need to use deliver(). Otherwise it is very difficult to update
        the DSMembers
        
        Complexity Worse Case: O(n)
        Complexity Best Case: O(n)
        """
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
        """
        Takes every DSMember and deliver its packages
        Complexity Worse Case: O(n^2)
        Complexity Best Case: O(n^2)
        """
        for _ in range(self.__DSMembers.size):
            member = self.__DSMembers.removeFirst()
            updated_member = self.deliverPackages(member)
            self.__DSMembers.addLast(updated_member.identifier, updated_member.name, updated_member.surname, updated_member.status)
            
    def removeDSMember(self,identifier):
        """
        Set to Inactive a DSMember using the identifier it has.
        And assigns the DMember's packages to the others DSMember
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        distributor = self.__DSMembers.removeById(identifier) 
        distributor.status = 'Inactive'
        if distributor.packetSize() != 0: 
            for _ in range(distributor.packetSize()):
                current_packet = distributor.deliver_packet()
                con = False
                i = 0
                while not con and i < self.__DSMembers.size:
                    current_staff = self.__DSMembers.getAt(i)
                    if current_staff.zones.contains(current_packet.post_code):
                        con = True
                        current_staff.assign_packet(current_packet)
                    i += 1
                if not con:
                    self.__Incidents.addLast(Incidents(current_packet.number, '', 'Staff unavailable')) 
                    print("The packet " + str(current_packet.number()) + "has been removed due to staff not being available") 
        self.__DSMembers.addLast(distributor.identifier, distributor.name, distributor.surname, distributor.status)                             
