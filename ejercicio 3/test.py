import unittest
import solucion

class TestMinJumps(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(solucion.calcular_saltos(1), 1)
        
    def test_case_2(self):
        self.assertEqual(solucion.calcular_saltos(2), 3)
        
    def test_case_3(self):
        self.assertEqual(solucion.calcular_saltos(3), 2)
        
    def test_case_4(self):
        self.assertEqual(solucion.calcular_saltos(4), 3)
        
    def test_case_5(self):
        self.assertEqual(solucion.calcular_saltos(5), 4)

if __name__ == "__main__":
    unittest.main()
