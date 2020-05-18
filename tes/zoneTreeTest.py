import unittest
from zoneTree import zoneTree

class ZoneTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = zoneTree()
        
    def testNodeSize(self):
        self.tree.createZone(1)
        self.tree.createZone(2)
        self.tree.createZone(3)
        result = self.tree.nodeSize(self.tree.root)
        assert result == 3
    
    def testSuccesorLeft(self):
        self.tree.createZone(10)
        self.tree.createZone(5)
        self.tree.createZone(6)
        self.tree.createZone(7)
        self.tree.createZone(9)
        result = self.tree.succesorLeft(self.tree.root)
        assert str(result) == "9"
        
    def testSuccesorRight(self):
        self.tree.createZone(1)
        self.tree.createZone(10)
        self.tree.createZone(9)
        self.tree.createZone(8)
        self.tree.createZone(5)
        result = self.tree.succesorRight(self.tree.root)
        assert str(result) == "5"
        
    def testDeleteZone(self):
        self.tree.createZone(1)
        self.tree.createZone(2)
        self.tree.createZone(3)
        self.tree.assignsDistributor(self.tree.root.Right,1,"Pablo", "Morales", "active")
        self.tree.deleteZone(self.tree.root.Right.Right)
        result1 = self.tree.nodeSize(self.tree.root) == 2
        result2 = self.tree.root.distributorSize() == 1
        assert result1 and result2
        
    def testAssignsDistributor(self):
        self.tree.createZone(1)
        self.tree.assignsDistributor(self.tree.root,1,"Pablo","Morales","active")
        result = self.tree.root.distributorSize()
        assert result == 1
        
    def testDeleteDistributor(self):
        self.tree.createZone(1)
        self.tree.assignsDistributor(self.tree.root,1,"Pablo","Morales","active")
        self.tree.assignsDistributor(self.tree.root,2,"Cristopher","Monzano","active")
        self.tree.deleteDistributor(self.tree.root,self.tree.root.getDistributor(1))
        result = self.tree.root.distributorSize()
        assert result == 1
        
    def testIsBalanced(self):
        self.tree.createZone(10)
        self.tree.createZone(5)
        self.tree.createZone(15)
        self.tree.createZone(12)
        self.tree.createZone(20)
        self.tree.isBalanced(self.tree.root)
        result = self.tree.isBalanced_Size(self.tree.root)
        assert result == True       
