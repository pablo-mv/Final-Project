#from srs.collection.DSMembers import DSMembers
from DSMembers import DSMembers

class zoneNode():
    """
    Atributes:
        zone: stores the zone number
        parent: stores the parent of this node
        childrenLeft: stores the left children of this node
        childrenRight: stores the right children of this node
        distributors: contains the list of distributiors of this zone
    """
    
    def __init__(self, zone, parent = None, chilLeft = None, chilRight = None):
        self.__zone = zone
        self.__parent = parent
        self.__childrenLeft = chilLeft
        self.__childrenRight = chilRight
        self.__distributors = DSMembers()
        
    def __str__(self):
        s = str(self.__zone)
        return s
     
    @property    
    def zone(self):
        return self.__zone
    @property
    def parent(self):
        return self.__parent
    @property
    def Right(self):
        return self.__childrenRight
    @property
    def Left(self):
        return self.__childrenLeft
    
    def newParent(self,t):
        """
        Initiallices or changes the parent of this node
        Complexity: 0(1)
        """
        self.__parent = t
        
    def newChildLeft(self,t):
        """
        Initiallices or changes the left child of this node
        Complexity: 0(1)
        """
        self.__childrenLeft = t
    
    def newChildRight(self,t):
        """
        Initiallices or changes the right child of this node
        Complexity: 0(1)
        """
        self.__childrenRight = t
    
    def showDistributors(self):
        """
        Returns a string with the names of all the distributors in this node
        Complexity: 0(n)
        """
        s = "The Distributros are: \n"
        for i in range(self.__distributors.size):
            name = self.__distributors.getAt(i)
            s = s + name.fullname() + "; \n"
        return s
    
    def assignDistributors(self, distributor):
        """
        Adds a new distributor the the distributor list
        Complexity: 0(1)
        """
        self.__distributors.addLast(distributor)
        
    def deleteDistributor(self, distributor):
        """
        Eliminates a specific distributor from this node
        Complexity: 0(1)
        """
        if distributor in self.__distributors:
            self.__distributors.pop(self.__distributors.index(distributor))
        else:
            print("Distributor not found in this zone")
            
#------------------------------------------------------------------------------
class zoneTree():
    """
    Atributes:
        size: The amount of nodes of the tree
        root: the first node of the tree
    """
    def __init__(self):
        self.__size = 0
        self.__root = None
        
    def createZone(self, zone, node = None):
        """
        Adds a new node to the tree, following the structure of a binary search tree
        Complexity: Worst O(log n), Best O(1)
        """
        newZone = zoneNode(zone)
        if self.__size == 0:
            self.__root = newZone
            self.__size = self.__size + 1
        else:
            if node == None:
                currentNode = self.__root
            else:
                currentNode = node
            
            if zone < currentNode.zone:
                if currentNode.Left() == None:
                    currentNode.newChildLeft(newZone)
                    newZone.newParent(currentNode)
                    self.__size = self.__size + 1
                else:
                    self.createZone(zone, currentNode.Left())
            elif zone > currentNode.zone:
                if currentNode.Right == None:
                    currentNode.newChildRight(newZone)
                    newZone.newParent(currentNode)
                    self.__size = self.__size + 1
                else:
                    self.createZone(zone, currentNode.Right)
                
    def showZones(self, node = None):
        """
        Shows all of the nodes of the tree if node = none, and 
        the subtre of node if node != none
        Complexity: Worst O(n^3), Best O(1)
        """
        if node == None:
            currentNode = self.__root
        else:
            currentNode = node
            
        if currentNode != None:
            print("Zone: " + str(currentNode.zone) + "\n" + currentNode.showDistributors())
            if currentNode.Left != None:
                self.showZones(currentNode.Left)
            if currentNode.Right != None:
                self.showZones(currentNode.Right)
            
    def nodeSize(self, node):
        """
        Returns the size of the subtree specified
        Complexity: Worst O(n^2), Best O(1)
        """
        if node == None:
            return -1
        return 1 + self.nodeSize(node.Left) + self.nodeSize(node.Right)
            
    def succesorLeft(self,node):
        currentNode = node.Left
        while currentNode.Right() != None:
            currentNode = currentNode.Right()
        return currentNode
    
    def succesorRight(self,node):
        currentNode = node.Right
        while currentNode.Left() != None:
            currentNode = currentNode.Left()
        return currentNode
    
    def findLowestAmountOfDistributors(self,node):
        node = zoneNode
        if node == None:
            return None, 0
        else:
            nodeLeft, minLeft = self.findLowestAmountOfDistributors(node.Left())
            nodeRight, minRight = self.findLowestAmountOfDistributors(node.Right())
            if minLeft < len(node.distributorList()) and minLeft < minRight:
                return nodeLeft, minLeft
            if minRight < len(node.distributorList()) and minRight < minLeft:
                return nodeRight, minRight
            if len(node.distributorList()) < minLeft and len(node.distributorList()) < minRight:
                return node, len(node.distributorList())
            
        
    def deleteZone(self, zone):
        zone = zoneNode()
        #Distributing the delivery men
        for i  in range(len(zone.distributorList())//2):
            nextNode = self.findLowestAmountOfDistributors(zone.Left)
            array = zone.distributorList()
            nextNode.assignDistributors(array.pop(i))
            
        for i  in range(len(zone.distributorList())//2, len(zone.distributorList())):
            nextNode = self.findLowestAmountOfDistributors(zone.Right)
            array = zone.distributorList()
            nextNode.assignDistributors(array.pop(i))
            
        #Eliminating the zone
        if self.__size == 1:
            self.__root = None
        elif zone.Left() != None and zone.Right() == None:
            zone.Left.newParent(zone.parent())
            if zone.parent == None:
                self.__root = zone.Left()
            zone.newParent(None)
            zone.newChildLeft(None)
        elif zone.Left() == None and zone.Right() != None:
            zone.Right.newParent(zone.parent())
            if zone.parent == None:
                self.__root = zone.Right()
            zone.newParent(None)
            zone.newChildRight(None)
        else:
            nextNode = self.succesorLeft(zone)
            nextNode = zoneNode()
            nextNode.newParent(zone.parent())
            if zone.parent() == None:
                self.__root = nextNode
            nextNode.newChildLeft = zone.Left
            nextNode.newChildRight = zone.Right
            zone.newParent(None)
            zone.newChildLeft(None)
            zone.newChildRight(None)
            
        
    def assignsDistributor(self, zone, dist):
        zone.assignDistributors(dist)
        
    def deleteDistributor(self,zone, dist):
        if dist not in zone.distributorList():
            print("Distributor not assigned to that zone")
        else:
            array = zone.distributorList()
            array.pop(array.index(dist))
            
    def showDistributor(self,node):
        node = zoneNode
        distList = node.distributorList
        sortedList = []
        for i in range(len(distList)):
            currentDist = distList[i]
            sortedList.append(currentDist.fullname())
        sortedList.sort()
        s = "The distributors of this zone are: \n"
        for i in sortedList:
            s = s + i + "\n"
        return s
    
    def isBalanced_Size(self, node):
        if self.nodeSize(node.Left) - self.nodeSize(node.Right) <= 1 and self.nodeSize(node.Left) - self.nodeSize(node.Right) >= -1:
            return True
        elif self.nodeSize(node.Left) - self.nodeSize(node.Right) > 1:
            return "l"
        elif self.nodeSize(node.Left) - self.nodeSize(node.Right) < -1:
            return "r"
    
    def isBalanced(self, node): #Doesnt work
        state = self.isBalanced_Size(node)
        if state:
            if node.Left != None:
                self.isBalanced(node.Left)
            if node.Right != None:
                self.isBalanced(node.Right)
                
                
        elif state == "l":
            newroot = node.Left
            while newroot.Right != None:
                newroot = newroot.Right
                
            newroot.parent = node.parent
            newroot.Left = node.Left
            newroot.Right = node.Right
            if node == self.__root:
                self.__root = newroot
                
            newparent = node.Right
            while newparent.Left != None:
                newparent = newparent.Left
            
            node.parent = newparent
            node.Left = None
            node.Right = None
            newparent.Left = node
            
            
        elif state == "r":
            newroot = node.Right
            while newroot.Left != None:
                newroot = newroot.Left
                
            newroot.parent = node.parent
            newroot.Right = node.Right
            newroot.Left = node.Left
            if node == self.__root:
                self.__root = newroot
                
            newparent = node.Left
            while newparent.Right != None:
                newparent = newparent.Right
            
            node.parent = newparent
            node.Left = None
            node.Right = None
            newparent.Left = node
            
    def head(self):
        return self.__root
                
        
#------------------------------------------------
tree = zoneTree()
tree.createZone(1)
print(tree.head()) 
tree.createZone(2)
print(tree.head()) 
tree.createZone(3)
tree.assignsDistributor(tree.head(),"1")
tree.showZones()


       
