from funciones import *
import unittest

class Test(unittest.TestCase):
    def test_diplomado(self):
        self.assertEqual(calcular_A(0, 0, 0, 0), 0)
        self.assertEqual(calcular_A(1, 0, 0, 0), 2)
        self.assertEqual(calcular_A(2, 0, 0, 0), 3)
        self.assertEqual(calcular_A(3, 0, 0, 0), 4)
        self.assertEqual(calcular_A(4, 0, 0, 0), 4)
        self.assertEqual(calcular_A(10, 0, 0, 0), 4)
    
    def test_especialidad(self):
        self.assertEqual(calcular_A(0, 0, 0, 0), 0)
        self.assertEqual(calcular_A(0, 1, 0, 0), 4)
        self.assertEqual(calcular_A(0, 2, 0, 0), 6)
        self.assertEqual(calcular_A(0, 10, 0, 0), 6)

    def test_maestria(self):
        self.assertEqual(calcular_A(0, 0, 0, 0), 0)
        self.assertEqual(calcular_A(0, 0, 1, 0), 8)
        self.assertEqual(calcular_A(0, 0, 2, 0), 11)
        self.assertEqual(calcular_A(0, 0, 10, 0), 11)

    def test_doctorado(self):
        self.assertEqual(calcular_A(0, 0, 0, 0), 0)
        self.assertEqual(calcular_A(0, 0, 0, 1), 12)
        self.assertEqual(calcular_A(0, 0, 0, 10), 12)

if __name__ == '__main__':
    unittest.main()