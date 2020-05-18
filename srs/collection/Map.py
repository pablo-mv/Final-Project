import sys

class deliveryPoint:
    def __init__(self, street, number, postalCode):
        self.id = str(street) + str(number) + str(postalCode)
        self.street = street
        self.number = number
        self.postalCode = postalCode
        self.neighbors = {}
    
    def addConection(self, neighbor, distance):
        if neighbor.id not in self.neighbors:
            self.neighbors[neighbor.id] = distance

    def removeConection(self, neighbor):
        try:
            self.neighbors.pop(neighbor.id)
        except:
            pass
    
    def getConections(self):
        return list(self.neighbors.items())

    def __str__(self):
        return str(self.street)+ ', ' + str(self.number) + ' ' + str(self.postalCode)
    

class Map:
    def __init__(self):
        self.__deliveryPoints = {}
    
    def __iter__(self):
        return iter(self.__deliveryPoints.values())

    def addDeliveryPoint(self, newDeliveryPoint):
        if newDeliveryPoint.id not in self.__deliveryPoints.keys():
            self.__deliveryPoints[newDeliveryPoint.id] = newDeliveryPoint
        else:
            print('There already exists this delivery point')

    def addConection(self, deliveryPointA, deliveryPointB, distance):
        deliveryPointA.addConection(deliveryPointB, distance)
        deliveryPointB.addConection(deliveryPointA, distance)

    def removeConection(self,deliveryPointA, deliveryPointB):
        deliveryPointA.removeConection(deliveryPointB)
        deliveryPointB.removeConection(deliveryPointA)
        

    def areConected(self, deliveryPointA, deliveryPointB):  
        # We are assuming that they are not directional links
        distance = -1
        for conection in deliveryPointB.getConections():
            if conection[0] == deliveryPointA.id:
                distance = conection[1]
        
        return distance
        
    def generateRoute(self):

        def _generateRoute(identifier, visited):
            visited[identifier] = True
            result.append(str(self.__deliveryPoints[identifier]))

            for adj in self.__deliveryPoints[identifier].getConections():
                if visited[adj[0]] == False:
                    _generateRoute(adj[0], visited)

        visited = {}
        result = []
        for point in self.__deliveryPoints.keys():
            visited[point] = False
        
        for identifier in self.__deliveryPoints.keys():
            if visited[identifier] == False:
                _generateRoute(identifier, visited)

        return result    
    

    def minRoute(self, start, end):
        visited ={}
        previous = {}
        distances = {}

        for i in self.__deliveryPoints.keys():
            visited[i] = False
            previous[i] = None
            distances[i] = sys.maxsize
        distances[start.id] = 0

        for _ in range(len(self.__deliveryPoints)):
            u = self.minDistance(distances, visited)
            visited[u] = True

            for neighbor in list(self.__deliveryPoints[u].neighbors.items()): 
                i=neighbor[0]
                w=neighbor[1]

                if visited[i]==False and distances[i]>distances[u]+w:
                    #we must update because its distance is greater than the new distance
                    distances[i]=distances[u]+w   
                    previous[i]=u
        
        self.printSolution(distances,previous,start, end)

    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        minimun = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for vertex in self.__deliveryPoints.keys(): 
            if distances[vertex] <= minimun and visited[vertex] == False: 
                minimun = distances[vertex] #update the new smallest
                min_vertex = vertex     #update the index of the smallest
        return min_vertex

    def printSolution(self,distances,previous,origin, end): 
        print("Mininum path from ",origin, 'to', end)
        for i, j in list(self.__deliveryPoints.items()):
            if j.id == end.id:
                if distances[i]==sys.maxsize:
                    print("There is not path from ",origin,' to ',j)
                else: 
                    #minimum_path is the list wich contains the minimum path from v to i
                    minimum_path=[]
                
                    prev=previous[j.id]
                    #this loop helps us to build the path
                    while prev!=None:
                        minimum_path.insert(0,prev[:-7]+', '+ prev[-7:-5]+' ' + prev[-5:])
                        prev=previous[prev]
                    
                    #we append the last vertex, which is i
                    minimum_path.append(str(j))  
                    #we print the path from v to i and the distance
                    print(origin,'->',j,":", minimum_path,distances[i])


myMap = Map()
v1 = deliveryPoint('A', 23, 28983)
v2 = deliveryPoint('B', 23, 23422)
v3 = deliveryPoint('C', 32, 33233)
v4 = deliveryPoint('D', 34, 32421)
v5 = deliveryPoint('E', 45, 32223)

myMap.addDeliveryPoint(v1)
myMap.addDeliveryPoint(v2)
myMap.addDeliveryPoint(v3)
myMap.addDeliveryPoint(v4)
myMap.addDeliveryPoint(v5)

myMap.addConection(v1, v3, 43)
myMap.addConection(v1, v2, 4)
myMap.addConection(v2, v3, 5)
myMap.addConection(v2, v5, 3)
myMap.addConection(v5, v4, 43)

print(myMap.generateRoute())
myMap.minRoute(v5, v1)
