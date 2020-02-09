import unittest
import CalculadoraComplejos
numero1=(-3,5)
numero2=(10,-8)
vectorreal1=[2,3]
vectorreal2=[4,5]
vector1=[[-2, 3], [4, -5]]
vector2=[[6, 7], [8, 9]]
matriz1=[[(2,3),(3,2)],[(3,1),(4,3)]]
matriz2=[[(1,1),(2,2)],[(3,3),(4,4)]]
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
        self.assertEqual(CalculadoraComplejos.conjugado(numero1),(-3, -5))
    def test_polar_cartesiano(self):
        self.assertEqual(CalculadoraComplejos.polar_cartesiano(numero1),(-2.988584094275237, -0.2614672282429745))
    def test_cartesiano_polar(self):
        self.assertEqual(CalculadoraComplejos.cartesiano_polar(numero1),(5.830951894845301, 120.96375653207352))
    def test_fase(self):
        self.assertEqual(CalculadoraComplejos.fase(numero1),(2.1112158270654806))
    def test_sumavector(self):
        self.assertEqual(CalculadoraComplejos.sumavector(vector1,vector2),([(4, 10), (12, 4)]))
    def test_inversovector(self):
        self.assertEqual(CalculadoraComplejos.inversovector(vector1),([(-2, -3), (4, 5)]))
    def test_producto_vectores(self):
        self.assertEqual(CalculadoraComplejos.producto_vectores(vector1,vector2),((44, 0)))
    def test_producto_interno(self):
        self.assertEqual(CalculadoraComplejos.producto_interno(vector1,vector2),((-4, 44)))
    def test_escalar_vector(self):
        self.assertEqual(CalculadoraComplejos.escalar_vector(numero1,vector1),([(-9, -19), (13, 35)]))
    def test_adicion_matrices(self):
        self.assertEqual(CalculadoraComplejos.adicion_matrices(matriz1,matriz2),([[(3, 4), (5, 4)], [(6, 4), (8, 7)]]))
    def test_matriz_inversa(self):
        self.assertEqual(CalculadoraComplejos.matriz_inversa(matriz1),([[(2, -3), (3, -2)], [(3, -1), (4, -3)]]))
    def test_escalar_matriz(self):
        self.assertEqual(CalculadoraComplejos.escalar_matriz(numero1,matriz1),([[(-21, 1), (-19, 9)], [(-14, 12), (-27, 11)]]))
    def test_transpuesta_matriz(self):
        self.assertEqual(CalculadoraComplejos.transpuesta_matriz(matriz1),([[(2, 3), (3, 1)], [(3, 2), (4, 3)]]))
    def test_transpuesta_vector(self):
        self.assertEqual(CalculadoraComplejos.transpuesta_vector(vector1),([[-2, 3], [4, -5]]))
    def test_conjugada_matriz(self):
        self.assertEqual(CalculadoraComplejos.conjugada_matriz(matriz1),([[(2, -3), (3, -2)], [(3, -1), (4, -3)]]))
    def test_conjugada_vector(self):
        self.assertEqual(CalculadoraComplejos.conjugada_vector(vector1),([(-2, -3), (4, 5)]))
    def test_adjunta_matriz(self):
        self.assertEqual(CalculadoraComplejos.adjunta_matriz(matriz1),([[(2, -3), (3, -1)], [(3, -2), (4, -3)]]))
    def test_adjunta_vector(self):
        self.assertEqual(CalculadoraComplejos.adjunta_vector(vector1),([(-2, -3), (4, 5)]))
    def test_producto_matrices(self):
        self.assertEqual(CalculadoraComplejos.producto_matrices(matriz1,matriz2),([[(2, 20), (2, 30)], [(5, 25), (8, 36)]]))
    def test_norma_vector(self):
        self.assertEqual(CalculadoraComplejos.norma_vector(vectorreal1),(3.605551275463989))
    def test_distancia_vectores(self):
        self.assertEqual(CalculadoraComplejos.distancia_vectores(vectorreal1,vectorreal2),(2.8284271247461903))
    def test_matriz_unitaria(self):
        self.assertEqual(CalculadoraComplejos.matriz_unitaria(matriz1),(False))
    def test_matriz_hermitiana(self):
        self.assertEqual(CalculadoraComplejos.matriz_hermitiana(matriz1),(False))
    def test_producto_tensor_vectores(self):
        self.assertEqual(CalculadoraComplejos.producto_tensor_vectores(vector1,vector2),([(-33, 4), (-43, 6), (59, -2), (77, -4)]))
    def test_producto_tensor_matrices(self):
        self.assertEqual(CalculadoraComplejos.producto_tensor_matrices(matriz1,matriz2),([[(-1, 5), (-2, 10), (1, 5), (2, 10)], [(-3, 15), (-4, 20), (3, 15), (4, 20)], [(2, 4), (4, 8), (1, 7), (2, 14)], [(6, 12), (8, 16), (3, 21), (4, 28)]]))
                         
if __name__ == "__main__":
    unittest.main()
            
