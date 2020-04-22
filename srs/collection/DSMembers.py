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
        
    def isEmpty(self):
        return self.size == 0
        
    def addFirst(self,e):
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
        if self.isEmpty():
            self.addFirst(e)
        else:
            newNode = DNode(e)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size = self.size + 1
            
    def removeFirst(self):
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
        r = None
        if n <= self.size:
            currentNode = self.head
            i = 0
            while i < n:
                currentNode = currentNode.next
                i = i + 1
            r = currentNode.elem
        return r
    
    def contains(self,e):
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
        if n == 1:
            self.addFirst(e)
        elif n == self.size:
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
        if n == 1:
            r = self.removeFirst
        elif n == self.size:
            r = self.removeLast
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
        currentNode = None
        nextNode = self.head
        for _ in range(self.size):
            currentNode = nextNode
            nextNode = currentNode.next
            con = False # Is this link sorted
            while not con and currentNode.prev != None:
                con = True
                currentSurname = currentNode.elem.surname()
                prevSurname = currentNode.prev.elem.surname()
                if currentSurname[0] < prevSurname[0]:
                    con = False
                    currentNext = currentNode.next                    
                    prevPrev = currentNode.next.next
                    currentNode.prev.next = currentNext
                    currentNode.prev.prev = currentNode
                    currentNode.next = currentNode.prev
                    currentNode.prev = prevPrev
                elif currentSurname[0] == prevSurname[0]: #In case two surnames start the same way
                    i = 0
                    while currentSurname[i] == prevSurname[i]:
                        i = i + 1
                    if currentSurname[i] < prevSurname[i]:
                        con = False
                        currentNext = currentNode.next                    
                        prevPrev = currentNode.next.next
                        currentNode.prev.next = currentNext
                        currentNode.prev.prev = currentNode
                        currentNode.next = currentNode.prev
                        currentNode.prev = prevPrev
