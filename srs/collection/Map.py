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

    def str2(self):
        s = str(self.street)+ ', ' + str(self.number) + ' ' + str(self.postalCode) + 'Conected to: \n'
        for i,j in list(self.neighbors.items()):
            s += '  ' + i[:-7]+', '+ i[-7:-5]+' ' + i[-5:] + ' with distande of ' + str(j) + '\n'
        return s

class Map:
    def __init__(self):
        self.__deliveryPoints = {}

    def __str__(self):
        r = ''
        for  i in iter(self):
            r += i.str2() + '\n\n'
        return r
    
    def __iter__(self):
        return iter(list(self.__deliveryPoints.values()))

    @property
    def deliveryPoints(self):
        return self.__deliveryPoints

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
        minimun = sys.maxsize 
        
        for vertex in self.__deliveryPoints.keys(): 
            if distances[vertex] <= minimun and visited[vertex] == False: 
                minimun = distances[vertex] 
                min_vertex = vertex     
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

