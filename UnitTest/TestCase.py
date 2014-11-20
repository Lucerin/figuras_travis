# -*- coding: utf8 -*-
# !usr/bin/env python
import unittest
from Figuras import Figuras


class TestCase(unittest.TestCase):

    def setUp(self):
        self.cal = Figuras()

    def test_usuario0(self):
        self.assertEqual(4, self.cal.cuadrado(2))

    def test_usuario01(self):
        self.assertEqual(
            18.847850000000005, self.cal.circulo(2.45))

    def test_usuario1(self):
        self.assertEqual(2, self.cal.rectangulo(2, 1))

    def test_usuario2(self):
        self.assertEqual(5, self.cal.triangulo(2, 5))

    def test_usuario3(self):
        self.assertEqual(8, self.cal.rombo(2, 8))

    def test_usuario4(self):
        self.assertEqual(25, self.cal.cuadrado(5))

    def test_usuario5(self):
        self.assertEqual(12.56, self.cal.circulo(2))

    def test_usuario6(self):
        self.assertEqual(14, self.cal.rectangulo(2, 7))

    def test_usuario7(self):
        self.assertEqual(3, self.cal.triangulo(2, 3))

    def test_usuario8(self):
        self.assertEqual(8, self.cal.rombo(2, 8))

    def test_usuario9(self):
        self.assertEqual(4, self.cal.cuadrado(2))

    def test_usuario10(self):
        self.assertEqual(113.04, self.cal.circulo(6))

    def test_usuario11(self):
        self.assertEqual(4, self.cal.rectangulo(2, 2))

    def test_usuario12(self):
        self.assertEqual(8, self.cal.triangulo(2, 8))

    def test_usuario13(self):
        self.assertEqual(4, self.cal.rombo(2, 4))

if __name__ == '__main__':
    unittest.main()
