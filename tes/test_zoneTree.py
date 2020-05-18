import sys
import os
sys.path.append(os.getcwd()) 

from srs.collection.zoneTree import zoneTree
import unittest

class TestAmazonManagment(unittest.TestCase):
    def setUp(self):
        #Aqui pones las cosas que necesitas definir desde el principio, como el zone tree
        #Esto se va a reiniciar antes de cada funcion
        #siempre pones el self para definir cosillas 
        # self.arbol = ZoneTree()

        pass

    def test_funcion(self):
        # Usa este formato, si no ponew test delante, no te reconce como un test

        
        assert True # assert es para comprobar si el test fue exitoso, recibe un boleano. La idea es poner: resulta == self.zoneTre.funcion()
        

if __name__ == '__main__': unittest.main()  # No lo entinedo, pero hae falta