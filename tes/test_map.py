import sys
import os
sys.path.append(os.getcwd())

import unittest
from srs.collection.Map import *

class TestMap(unittest.TestCase):

    def setUp(self):
        self.map = Map()
        self.v1 = deliveryPoint('A', 23, 28983)
        self.v2 = deliveryPoint('B', 23, 23422)
        self.v3 = deliveryPoint('C', 32, 33233)
        self.v4 = deliveryPoint('D', 34, 32421)
        self.v5 = deliveryPoint('E', 45, 32223)

        self.map.addDeliveryPoint(self.v1)
        self.map.addDeliveryPoint(self.v2)
        self.map.addDeliveryPoint(self.v3)
        self.map.addDeliveryPoint(self.v4)
        self.map.addDeliveryPoint(self.v5)
        

    def test_addDeliveryPoint(self):
        v9 = deliveryPoint('Avenida de los planetas', 23, 28983)
        self.map.addDeliveryPoint(v9)
        
        assert self.v1.id in list(self.map.deliveryPoints.keys())

    def test_addConnection(self):
        self.map.addConection(self.v1, self.v3, 23)

        assert -1 != self.map.areConected(self.v1, self.v3)

    def test_removeConection(self):
        self.map.addConection(self.v1,self.v3, 50)
        self.map.removeConection(self.v1,self.v3)

        assert -1 == self.map.areConected(self.v1, self.v3)

    def test_areConnected(self):
        self.map.addConection(self.v1, self.v4, 432)
        yes = self.map.areConected(self.v1, self.v4)
        no = self.map.areConected(self.v1, deliveryPoint('sd', 23, 32123))
        
        assert yes != -1 and no == -1

    def test_generateRoute(self):
        self.map.addConection(self.v1, self.v2, 1)
        self.map.addConection(self.v1, self.v3, 1)
        self.map.addConection(self.v2, self.v4, 1)
        self.map.addConection(self.v2, self.v5, 1)

        dfs = self.map.generateRoute()
        
        assert ['A, 23 28983', 'B, 23 23422', 'D, 34 32421', 'E, 45 32223', 'C, 32 33233'] == dfs

    def test_minRoute(self):
        error = False
        try:
            self.map.addConection(self.v1, self.v2, 1)
            self.map.addConection(self.v2, self.v4, 1)
            self.map.addConection(self.v2, self.v5, 1)

            self.map.minRoute(self.v1, self.v1)
            print('')
            self.map.minRoute(self.v1, self.v3)
            print('')
            self.map.minRoute(self.v5, self.v2)
            print('')
            self.map.minRoute(self.v1, self.v4)
            print('')
        except:
            error = True
        assert error == False

    def test_str(self):
        error = False
        try:
            self.map.addConection(self.v1, self.v2, 2)
            self.map.addConection(self.v2, self.v4, 1)
            self.map.addConection(self.v2, self.v5, 23)
            print(self.map)
        except:
            error = True
        
        assert error == False

if __name__ == '__main__': unittest.main()