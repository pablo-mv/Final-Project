import sys
import os
sys.path.append(os.getcwd())

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
    def __init__(self, ident, name, surname, status, zones=None, packets=None, nexts = None, prev = None):
        if (isinstance(ident, int) and len(str(ident)) <= 6):
            ceros_extra = 6 - len(str(ident))
            ceros = ''
            for _ in range (ceros_extra):
                ceros += '0'
            self.__identifier = "R" + ceros +str(ident)
            self.__id = ident
        else:
            print("Error - identifier must follow the structure XXXXXX, with X being a number")
            self.__id = 999999

        self.__name = name
        self.__surname = surname
        self.__status = status

        if packets == None:
            self.__packets = DList()
        else:
            self.__packets = packets
        
        if zones == None:
            self.__zones = DList()
        else:
            self.__zones = zones
        
        self.next = nexts
        self.prev = prev
        surname
    
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
        s = self.__surname + ", "  + self.__name 
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
        return self.__id
    
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
    
    @property
    def packets(self):
        return self.__packets
    
        
    
    
#------------------------------------------------------------------------------
class DSMembers():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
        
    def __str__(self):
        """
        Gives all of the members information in string form
        Complexity: Worst O(n), Best O(1)
        """
        s = "< \n"
        if self.isEmpty():
            s += ">"
        else:
            currentNode = self.__head
            while currentNode != None:
                s = s + str(currentNode) + ", \n"
                currentNode = currentNode.next
            s = s + ">"
        return s
    
    def isEmpty(self):
        """
        Returns True if there are not DSMember and False otherwise
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        return self.__size == 0
    
    def addFirst(self,ident, name, surname, status, zones = None, packets = None):
        """
        Inserts a DSMember in the first place
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        newNode = DSMember(ident, name, surname, status, zones, packets)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
        self.__size = self.__size + 1

    def addLast(self, ident, name, surname, status, zones = None, packets = None):
        """
        Inserts a DSMember in the last place
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        if self.isEmpty():
            self.addFirst(ident, name, surname, status, zones = None, packets = None)
        else:
            newNode = DSMember(ident, name, surname, status, zones , packets )
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
            self.__size = self.__size + 1
            
    def removeFirst(self):
        """
        Removes the first DSMmber and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        r = None
        if not self.isEmpty():
            r = self.__head
            self.__head = self.__head.next
            if self.__size == 1:
                self.__head = None
                self.__tail = None
            else:
                self.__head.prev = None
            self.__size = self.__size - 1
        return r
    
    def removeLast(self):
        """
        Removes the last DSMember and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        r = None
        if not self.isEmpty():
            r = self.__tail
            self.__tail = self.__tail.prev
            if self.__size == 1:
                self.__head == None
                self.__tail == None
            else:
                self.__tail.next = None
            self.__size = self.__size - 1
        return r
            
    def getAt(self,n):
        """
        Returns the element of the node of the index given
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        r = None
        if n == 0:
            r = self.__head
        elif n == self.__size - 1:
            r = self.__tail
        elif n <= self.__size:
            currentNode = self.__head
            i = 1
            while i <= n:
                currentNode = currentNode.next
                i = i + 1
                
            r = currentNode
        return r
        
    def contains(self,e):
        """
        Returns True if the list contains the DSMember, false otherwise
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        r = False
        currentNode = self.__head
        i = 0
        while i < self.__size and not r:
            if currentNode == e:
                r = True
            else:
                currentNode = currentNode.next()
                i = i + 1
        return r
    
    def insertAt(self, n, ident, name, surname, status, zones = None, packets = None):
        """
        Inserts a DSMember in the position n
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        if n == 0:
            self.addFirst(ident, name, surname, status, zones, packets)
        elif n >= self.__size:
            self.addLast(ident, name, surname, status, zones, packets)
        else:
            newNode = DSMember(ident, name, surname, status, zones, packets)
            i = 1
            currentNode = self.__head
            while i < n:
                currentNode = currentNode.next
                i = i + 1
            newNode.prev = currentNode
            newNode.next = currentNode.next
            currentNode.next.prev = newNode
            currentNode.next = newNode
            self.__size = self.__size + 1

    def removeAt(self,n):
        """
        Removes the DSMember of the position n and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        if n == 0:
            r = self.removeFirst()
        elif n == self.__size - 1:
            r = self.removeLast()
        else:
            i = 1
            currentNode = self.__head
            while i <= n:
                currentNode = currentNode.next
                i = i + 1
            r = currentNode
            prevNode = currentNode.prev
            nextNode = currentNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.__size = self.__size - 1
        return r

    def sortAlphabeticalSurname(self):
        """
        Is a kind of bubble sort with letters.
        Complexity Worse Case: O(n^2)
        Complexity Best Case: O(n^2)
        """
        for _ in range(self.size):

            if self.__head != None:    
                currentNode = self.__head
                nextNode = self.__head.next
                if nextNode != None:
                    i = self.size -1
                    while i > 0:
                        if currentNode.surname > nextNode.surname:
                            isHead = isTail = False
                            try:
                                currentNode.prev.next = nextNode
                            except:
                                isHead = True

                            try:
                                nextNode.next.prev = currentNode
                            except:
                                isTail = True

                            currentNode.next = nextNode.next
                            nextNode.prev = currentNode.prev
                            
                            
                            currentNode.prev = nextNode
                            nextNode.next = currentNode
                            
                            aux = currentNode
                            currentNode = nextNode
                            nextNode = aux
                            if isHead:
                                self.__head = currentNode
                            if isTail:
                                self.__tail = nextNode
                            

                        currentNode = currentNode.next
                        nextNode = nextNode.next
                        i -= 1
                    
                    
    
    def removeById(self, identifier):
        result = None

        currentNode = self.__tail
        if currentNode != None:
            if currentNode.identifier == identifier:
                    result = currentNode
                    try:
                        currentNode.prev.next = None
                    except:
                        pass
                    self.__tail = currentNode.prev
        
        currentNode = self.__head
        if currentNode != None:
            if currentNode.identifier == identifier:
                    result = currentNode
                    currentNode.next.prev = None
                    self.__head = currentNode.next
            else:
                while currentNode.next != None:
                    if currentNode.identifier == identifier:
                        result = currentNode
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev
                    currentNode = currentNode.next

        if result != None:
            self.__size -= 1
            
        return result
    
    def addWholeDistributor(self,dist):
        self.addLast(dist)
            
    @property
    def size(self):
        return self.__size                
                    
    @property
    def head(self):
        return self.__head
    
"""        
lis = DSMembers()        
print(lis.isEmpty())     
lis.addFirst(1,"Pablo","Morales","active")
lis.addLast(2,"Cristopher","Manzanos","active")
lis.insertAt(1,3,"Alejandro", "Pares", "active")
#print(lis.getAt(0))
print("\n")
#print(lis.getAt(1))
print("\n")
#print(lis.getAt(2))
print("-------------------- \n")  
lis.sortAlphabeticalSurname()
print("\n")
print(lis.getAt(0))
print("\n")  
print(lis.getAt(1))
print("\n")
print(lis.getAt(2))
"""
