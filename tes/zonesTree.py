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
    
    def assignDistributors(self, ident, name, surname, status):
        """
        Adds a new distributor the the distributor list
        Complexity: 0(1)
        """
        self.__distributors.addLast(ident, name, surname, status)
        
    def deleteDistributor(self, distributor):
        """
        Eliminates a specific distributor from this node
        Complexity: 0(1)
        """
        if self.__distributors.contains(distributor):
            self.__distributors.removeById(distributor.identifier)
        else:
            print("Distributor not found in this zone")
            
    def getDistributor(self,n):
        return self.__distributors.getAt(n)
    def distributorSize(self):
        return self.__distributors.size
    def removeDistAt(self,n):
        return self.__distributors.removeAt(n)
    def containsDist(self,dist):
        return self.__distributors.contains(dist)
    def removeDistID(self,ids):
        return self.__distributors.removeById(ids)
    def sortDistAbc(self):
        self.__distributors.sortAlphabeticalSurname()
    def addWholeDistributor(self,dis):
        self.__distributors.addWholeDistributor(dis)
            
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
        
    def createZone(self, zone_n, node = None):
        """
        Adds a new node to the tree, following the structure of a binary search tree
        Complexity: Worst O(log n), Best O(1)
        """
        newZone = zoneNode(zone_n)
        if self.__size == 0:
            self.__root = newZone
            self.__size = self.__size + 1
        else:
            if node == None:
                currentNode = self.__root
            else:
                currentNode = node
            
            if zone_n < currentNode.zone:
                if currentNode.Left == None:
                    currentNode.newChildLeft(newZone)
                    newZone.newParent(currentNode)
                    self.__size = self.__size + 1
                else:
                    self.createZone(zone_n, currentNode.Left)
            elif zone_n > currentNode.zone:
                if currentNode.Right == None:
                    currentNode.newChildRight(newZone)
                    newZone.newParent(currentNode)
                    self.__size = self.__size + 1
                else:
                    self.createZone(zone_n, currentNode.Right)
                
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
        if node != None:
            return 1 + self.nodeSize(node.Left) + self.nodeSize(node.Right)
        else:
            return 0
            
    def succesorLeft(self,node):
        """
        Returns the highest value in its left subtree
        Complextiy: O(n)
        """
        currentNode = node.Left
        while currentNode.Right != None:      
            currentNode = currentNode.Right
        return currentNode
    
    def succesorRight(self,node):
        """
        Returns the lowest value in its right subtree
        Complextiy: O(n)
        """
        currentNode = node.Right
        while currentNode.Left != None:
            currentNode = currentNode.Left
        return currentNode
            
        
    def deleteZone(self, zone):
        """
        Returns the node with the lowest amount of distributors
        """
        if zone.Left != None and zone.Right != None and zone.parent != None:
            for i in range(zone.distributorSize()//3):
                zone.Left.addWholeDistributor(zone.removeDistAt(0))
            for i in range(zone.distributorSize()//3,2*zone.distributorSize()//3,):
                zone.Right.addWholeDistributor(zone.removeDistAt(0))
            for i in range(2*zone.distributorSize()//3,3*zone.distributorSize()//3,):
                zone.Right.addWholeDistributor(zone.removeDistAt(0))
        elif zone.Left != None and zone.Right != None:
            for i in range(zone.distributorSize()//2):
                zone.Left.addWholeDistributor(zone.removeDistAt(0))
            for i in range(zone.distributorSize()//2,2*zone.distributorSize()//2,):
                zone.Right.addWholeDistributor(zone.removeDistAt(0))
        elif zone.Left != None and zone.parent != None:
            for i in range(zone.distributorSize()//2):
                zone.Left.addWholeDistributor(zone.removeDistAt(0))
            for i in range(zone.distributorSize()//2,2*zone.distributorSize()//2,):
                zone.parent.addWholeDistributor(zone.removeDistAt(0))
        elif zone.Right != None and zone.parent != None:
            for i in range(zone.distributorSize()//2):
                zone.Right.addWholeDistributor(zone.removeDistAt(0))
            for i in range(zone.distributorSize()//2,2*zone.distributorSize()//2,):
                zone.parent.addWholeDistributor(zone.removeDistAt(0))
        elif zone.Left != None:
            for i in range(zone.distributorSize()):
                zone.Left.addWholeDistributor(zone.removeDistAt(0))
        elif zone.Right != None:
            for i in range(zone.distributorSize()):
                zone.Right.addWholeDistributor(zone.removeDistAt(0))
        elif zone.parent != None:
            for i in range(zone.distributorSize()):
                zone.parent.addWholeDistributor(zone.removeDistAt(0))
            
                
            
            
        #Eliminating the zone
        if self.__size == 1:
            self.__root = None
        elif zone.Left != None and zone.Right == None:
            zone.Left.newParent(zone.parent)
            if zone.parent == None:
                self.__root = zone.Left
            zone.newParent(None)
            zone.newChildLeft(None)
        elif zone.Left == None and zone.Right != None:
            zone.Right.newParent(zone.parent)
            if zone.parent == None:
                self.__root = zone.Right
            zone.newParent(None)
            zone.newChildRight(None)
        else:
            nextNode = self.succesorLeft(zone)
            nextNode = zoneNode()
            nextNode.newParent(zone.parent)
            if zone.parent == None:
                self.__root = nextNode
            nextNode.newChildLeft = zone.Left
            nextNode.newChildRight = zone.Right
            zone.newParent(None)
            zone.newChildLeft(None)
            zone.newChildRight(None)
            
        
    def assignsDistributor(self, zone, ident, name, surname, status):
        """
        Assigns a distributor to a zone
        """
        zone.assignDistributors(ident, name, surname, status)
        
    def deleteDistributor(self,zone, dist):
        """
        Deletes a distributor
        """
        if not zone.containsDist(dist):
            print("Distributor not assigned to that zone")
        else:
            zone.removeDistID(dist.identifier)
            
    def showDistributor(self,node):
        """
        Shows all of the distributors of a node
        """
        node.sortDistAbc()
        s = "The distributors of this zone are: \n"
        for i in range(node.distributorSize()):
            s = s + str(node.getDistributor(i)) + "\n"
        print( s)
    
    def isBalanced_Size(self, node):
        """
        Checks if the tree is balanced by size, and returns a value accordingly
        """
        if self.nodeSize(node.Left) - self.nodeSize(node.Right) <= 1 and self.nodeSize(node.Left) - self.nodeSize(node.Right) >= -1:
            return True
        elif self.nodeSize(node.Left) - self.nodeSize(node.Right) > 1:
            return "l"
        elif self.nodeSize(node.Left) - self.nodeSize(node.Right) < -1:
            return "r"
    
    def isBalanced(self, node): 
        """
        Balances the tree if its not balanced
        """
        state = self.isBalanced_Size(node)       
        if state == "l":
            newRoot = self.succesorRight(self.__root)
            oldRoot = self.__root
            newRoot.parent.newChildRight(None)
            newRoot.newParent(None)
            if oldRoot.Right != None:
                prevOldRoot = self.succesorRight(oldRoot)
                prevOldRoot.newChildLeft(oldRoot)
                oldRoot.newParent(prevOldRoot)
                newRoot.newChildRight(oldRoot.Right)
                oldRoot.newChildRight(None)
                newRoot.newChildLeft(oldRoot.Left)
                oldRoot.newChildLeft(None)
                self.__root = newRoot
            else:
                newRoot.newChildLeft(oldRoot.Left)
                newRoot.newChildRight(oldRoot)
                oldRoot.newParent(newRoot)
                oldRoot.newChildLeft(None)
                self.__root = newRoot
        
        
        elif state == "r":
            newRoot = self.succesorRight(self.__root)
            oldRoot = self.__root
            newRoot.parent.newChildLeft(None)
            newRoot.newParent(None)
            if oldRoot.Left != None:
                prevOldRoot = self.succesorLeft(oldRoot)
                prevOldRoot.newChildRight(oldRoot)
                oldRoot.newParent(prevOldRoot)
                newRoot.newChildLeft(oldRoot.Left)
                oldRoot.newChildLeft(None)
                newRoot.newChildRight(oldRoot.Right)
                oldRoot.newChildRight(None)
                self.__root = newRoot
            else:
                newRoot.newChildRight(oldRoot.Right)
                newRoot.newChildLeft(oldRoot)
                oldRoot.newParent(newRoot)
                oldRoot.newChildRight(None)
                self.__root = newRoot
        
        if state == True:
            if node.Left != None:
                self.isBalanced(node.Left)
            if node.Right != None:
                self.isBalanced(node.Right)    
                
         
    @property        
    def root(self):
        return self.__root
