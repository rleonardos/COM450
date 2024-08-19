from funciones import *
import unittest

class Test(unittest.TestCase):
    def test_publicacion(self):
        self.assertEqual(calcular_D(0), 0)
        self.assertEqual(calcular_D(1), 1)
        self.assertEqual(calcular_D(2), 2)
        self.assertEqual(calcular_D(3), 2)

if __name__ == '__main__':
    unittest.main()