from funciones import *
import unittest

class Test(unittest.TestCase):
    def test_antiguedad(self):
        self.assertEqual(calcular_C(0,0,0), 0)
        self.assertEqual(calcular_C(1,0,0), 1)
        self.assertEqual(calcular_C(2,0,0), 2)
        self.assertEqual(calcular_C(3,0,0), 3)
        self.assertEqual(calcular_C(4,0,0), 4)
        self.assertEqual(calcular_C(5,0,0), 4)

    def test_servidor(self):
        self.assertEqual(calcular_C(0,0,0), 0)
        self.assertEqual(calcular_C(0,1,0), 1)
        self.assertEqual(calcular_C(0,2,0), 2)
        self.assertEqual(calcular_C(0,3,0), 3)
        self.assertEqual(calcular_C(0,4,0), 4)
        self.assertEqual(calcular_C(0,5,0), 4)

    def test_docente(self):
        self.assertEqual(calcular_C(0,0,0), 0)
        self.assertEqual(calcular_C(0,0,1), 2)
        self.assertEqual(calcular_C(0,0,2), 2)

if __name__ == '__main__':
    unittest.main()