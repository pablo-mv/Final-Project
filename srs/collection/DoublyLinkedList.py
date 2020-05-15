class DNode:
    def __init__(self,e, nexts = None, prev = None):
        self.elem = e
        self.next = nexts
        self.prev = prev
        
#---------------------------------------------------------------------
class DList:
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
            self.tail.next = newNode
            newNode.prev = self.tail
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
            i = 1
            while i <= n:
                currentNode = currentNode.next
                i = i + 1
            r = currentNode.elem
        return r
    
    def contains(self,e):
        con = False
        if self.isEmpty():
            return con
        currentNode = self.head
        while currentNode.next != None and not con:
            if currentNode.elem == e:
                return True
            currentNode = currentNode.next
        if currentNode.elem == e:
            return True
        return con
    
    def insertAt(self,n,e):
        if n == 0:
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
        if n == 0:
            r = self.removeFirst()
        elif n == self.size - 1:
            r = self.removeLast()
        else:
            i = 1
            currentNode = self.head
            while i <= n:
                currentNode = currentNode.next
                i = i + 1
            r = currentNode.elem
            prevNode = currentNode.prev
            nextNode = currentNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.size = self.size - 1
        return r
                
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
        
