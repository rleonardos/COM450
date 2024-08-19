from calificacion import *
import unittest

class Test(unittest.TestCase):
    def test_asistencia(self):
        self.assertEqual(calcular_B(0), 0)
        self.assertEqual(calcular_B(1), 0.5)
        self.assertEqual(calcular_B(2), 1)
        self.assertEqual(calcular_B(3), 1.5)
        self.assertEqual(calcular_B(4), 2)
        self.assertEqual(calcular_B(5), 2.5)
        self.assertEqual(calcular_B(6), 3)
        self.assertEqual(calcular_B(7), 3.5)
        self.assertEqual(calcular_B(8), 4)
        self.assertEqual(calcular_B(9), 4.5)
        self.assertEqual(calcular_B(10), 5)
        self.assertEqual(calcular_B(11), 5.5)
        self.assertEqual(calcular_B(12), 6)
        self.assertEqual(calcular_B(20), 6)

if __name__ == '__main__':
    unittest.main()