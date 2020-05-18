import sys
import os
sys.path.append(os.getcwd())

import unittest
from srs.collection.Map import *

class TestMap(unittest.TestCase):

    def setUp(self):
        self.map = Map()
        v1 = deliveryPoint('A', 23, 28983)
        v2 = deliveryPoint('B', 23, 23422)
        v3 = deliveryPoint('C', 32, 33233)
        v4 = deliveryPoint('D', 34, 32421)
        v5 = deliveryPoint('E', 45, 32223)
    def test_addDeliveryPoint(self):


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