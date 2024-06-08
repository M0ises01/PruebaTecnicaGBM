import unittest
import solucion

class TestPalindromo(unittest.TestCase):
    
    def test_palindromo_simple(self):
        self.assertTrue(solucion.es_palindromo("Ana"))
        
    def test_no_palindromo(self):
        self.assertFalse(solucion.es_palindromo("Python"))
        
    def test_palindromo_con_espacios_y_signos(self):
        self.assertTrue(solucion.es_palindromo("A man, a plan, a canal, Panama"))

if __name__ == "__main__":
    unittest.main()
