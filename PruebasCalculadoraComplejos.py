import unittest
import CalculadoraComplejos
numero1=(-3,5)
numero2=(10,-8)
class TestCases(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(CalculadoraComplejos.sumar(numero1,numero2),(7,-3))
    def test_multiplicarr(self):
        self.assertEqual(CalculadoraComplejos.multiplicar(numero1,numero2),(10,74))
    def test_restar(self):
        self.assertEqual(CalculadoraComplejos.restar(numero1,numero2),(-13,13))
    def test_dividir(self):
        self.assertEqual(CalculadoraComplejos.dividir(numero1,numero2),(-0.4268292682926829, 0.15853658536585366))
    def test_modulo(self):
        self.assertEqual(CalculadoraComplejos.modulo(numero1),(5.830951894845301))
    def test_conjugado(self):
        self.assertEqual(CalculadoraComplejos.conjugado(numero1),(3, -5))
    def test_polar_cartesiano(self):
        self.assertEqual(CalculadoraComplejos.polar_cartesiano(numero1),(-2.988584094275237, -0.2614672282429745))
    def test_cartesiano_polar(self):
        self.assertEqual(CalculadoraComplejos.cartesiano_polar(numero1),(5.830951894845301, 120.96375653207352))
    def test_fase(self):
        self.assertEqual(CalculadoraComplejos.fase(numero1),(2.1112158270654806))
if __name__ == "__main__":
    unittest.main()
            
