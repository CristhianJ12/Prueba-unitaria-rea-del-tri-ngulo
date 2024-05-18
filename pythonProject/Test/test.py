import unittest
import math

# Función para calcular el área del triángulo con base y altura conocidas
def area_base_altura(base, altura):
    area = 0.5 * base * altura
    return area

# Función para calcular el área del triángulo con longitudes de los tres lados conocidos
def area_lados(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Clase de prueba
class TestAreaTriangulo(unittest.TestCase):

    def test_base_altura(self):
        self.assertEqual(area_base_altura(12, 6), 36)  # Caso 3
        self.assertEqual(area_base_altura(9, 4), 18)   # Caso 4
        self.assertEqual(area_base_altura(15, 10), 75) # Caso 5

    def test_lados(self):
        self.assertEqual(area_lados(5, 12, 13), 30)    # Caso 6
        self.assertEqual(area_lados(8, 15, 17), 60)    # Caso 7
        self.assertEqual(area_lados(3, 4, 5), 6)       # Caso 8
        self.assertEqual(area_lados(6, 8, 10), 24)     # Caso 9
        self.assertEqual(area_lados(9, 12, 15), 54)    # Caso 10

if __name__ == '__main__':
    unittest.main()
