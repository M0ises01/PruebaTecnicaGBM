import unittest
import numpy as np
import solucion

class TestCustomerClassification(unittest.TestCase):
    
    def test_case_1(self):
        entradas = np.array([[1, 10, 20]])
        resultado_esperado = [0]
        resultado = solucion.predecir_categoria(entradas)
        self.assertEqual(resultado.tolist(), resultado_esperado)
        
    def test_case_2(self):
        entradas = np.array([[15, 700, 101]])
        resultado_esperado = [1]
        resultado = solucion.predecir_categoria(entradas)
        self.assertEqual(resultado.tolist(), resultado_esperado)
        
    def test_case_3(self):
        entradas = np.array([[20, 2000, 200]])
        resultado_esperado = [2]
        resultado = solucion.predecir_categoria(entradas)
        self.assertEqual(resultado.tolist(), resultado_esperado)
        
    def test_case_4(self):
        entradas = np.array([[1, 10, 20], [15, 700, 101], [20, 2000, 200]])
        resultado_esperado = [0, 1, 2]
        resultado = solucion.predecir_categoria(entradas)
        self.assertEqual(resultado.tolist(), resultado_esperado)
        
    def test_case_5(self):
        entradas = np.array([[5, 300, 50], [10, 900, 150], [30, 1500, 300]])
        resultado_esperado = [0, 1, 2]
        resultado = solucion.predecir_categoria(entradas)
        self.assertEqual(resultado.tolist(), resultado_esperado)

if __name__ == "__main__":
    unittest.main()
