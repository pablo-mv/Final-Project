class DNode:
    def __init__(self,e, nexts = None, prev = None):
        self.elem = e
        self.next = nexts
        self.prev = prev
        
        
#---------------------------------------------------------------------
class DSMembers:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        s = '<'
        if self.isEmpty():
            s += '>'
        else:
            currentNode = self.head
            while currentNode.next != None:
                s += str(currentNode.elem) + ', '
                currentNode = currentNode.next
            s += str(currentNode.elem)  + '>'
        return s
        
    def isEmpty(self):
        """
        Returns True if there are not DSMember and False otherwise
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        return self.size == 0
        
    def addFirst(self,e):
        """
        Inserts a DSMember in the first place
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        newNode = DNode(e)
        if self.isEmpty():
            self.tail = newNode
            self.head = newNode
        else:
           newNode.next = self.head
           self.head.prev = newNode
           self.head = newNode
        self.size = self.size + 1
            
    def addLast(self,e):
        """
        Inserts a DSMember in the last place
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        if self.isEmpty():
            self.addFirst(e)
        else:
            newNode = DNode(e)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size = self.size + 1
            
    def removeFirst(self):
        """
        Removes the first DSMmber and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        r = None
        if not self.isEmpty():
            r = self.head.elem
            self.head = self.head.next
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head.prev = None
            self.size = self.size - 1
        return r
    
    def removeLast(self):
        """
        Removes the last DSMember and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(1)
        """
        r = None
        if not self.isEmpty():
            r = self.tail.elem
            self.tail = self.tail.prev
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.next = None
            self.size = self.size - 1
        return r
    
    def getAt(self,n):
        """
        Returns the element of the node of the index given
        Complexity Worse Case: O(n)
        Complexity Best Case: O(1)
        """
        r = None
        if n == 0:
            r = self.head.elem
        elif n <= self.size:
            currentNode = self.head
            i = 1
            while i < n:
                currentNode = currentNode.next
                i = i + 1
            
            r = currentNode.elem
        return r
    
    def contains(self,e):
        """
        Returns True if the list contains the DSMember, false otherwise
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        r = -1
        con = True
        i = 0
        currentNode = self.head
        while i < self.size and con:
            if currentNode.elem == e:
                con = False
                r = i
            currentNode = currentNode.next
            i = i + 1
        return r
    
    def insertAt(self,n,e):
        """
        Inserts a DSMember in the position n
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        if n == 1:
            self.addFirst(e)
        elif n >= self.size:
            self.addLast(e)
        else:
            newNode = DNode(e)
            i = 1
            currentNode = self.head
            while i < n:
                currentNode = currentNode.next
                i = i + 1
            newNode.prev = currentNode
            newNode.next = currentNode.next
            currentNode.next.prev = newNode
            currentNode.next = newNode
            self.size = self.size + 1
            
    def removeAt(self,n):
        """
        Removes the DSMember of the position n and returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        if n == 1:
            r = self.removeFirst()
        elif n == self.size:
            r = self.removeLast()
        else:
            i = 1
            currentNode = self.head
            while i < n:
                currentNode = currentNode.next
                i = i + 1
            r = currentNode.elem
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            self.size = self.size - 1
        return r
                
    def sortAlphabeticalSurname(self):
        """
        Is a kind of bubble sort with letters.
        Complexity Worse Case: O(n^2)
        Complexity Best Case: O(n^2)
        """
        for _ in range(self.size):
            try:
                currentNode = self.head
                nextNode = self.head.next
                i = 0
                if nextNode != None:
                    while nextNode.next != None:
                        i = 0
                        while currentNode.elem.fullname()[i] == nextNode.elem.fullname()[i] and i <min(len(currentNode.elem.fullname()), len(nextNode.elem.fullname())-1):
                            i += 1
                            """
                            If the names are repeated, it iterates until get 
                            an index with a letter diferent or reaching the max size
                            """
                        
                        if currentNode.elem.fullname()[i] > nextNode.elem.fullname()[i]:
                            aux = currentNode.elem
                            currentNode.elem = nextNode.elem
                            nextNode.elem = aux
                        currentNode = nextNode
                        nextNode = nextNode.next
                    
                    if currentNode.elem.fullname()[i] > nextNode.elem.fullname()[i]:
                        aux = currentNode.elem
                        currentNode.elem = nextNode.elem
                        nextNode.elem = aux
            except:
                pass
            
                
    def removeById(self, identifier):
        """
        Removes a DSMember with the identifier the member has. And returns it.
        Complexity Best Case: O(1)
        Complexity Worst Case: O(n)
        """
        r = None 
        if self.head.elem.identifier == identifier:
            r = self.removeFirst()
        
        elif self.tail.elem.identifier == identifier:
            r = self.removeLast()
        elif self.head !=None:
            currentNode = self.head
            while currentNode.next != None and r == None:
                if currentNode.elem.identifier == identifier:
                    r = currentNode.elem
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                else:
                    currentNode = currentNode.next
        return r
                
