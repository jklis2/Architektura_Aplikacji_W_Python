# -*- coding: utf-8 -*-
import unittest
from zadanie_1_class import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Laptop", 1500, 10)

    def test_add_to_stock(self):
        self.product.add_to_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_remove_from_stock(self):
        self.product.remove_from_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_from_stock_not_enough_stock(self):
        with self.assertRaises(ValueError):
            self.product.remove_from_stock(15)

    def test_remove_from_stock_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.product.remove_from_stock(-3)

    def test_add_to_stock_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.product.add_to_stock(-5)

    def test_is_available(self):
        self.assertTrue(self.product.is_available())

    def test_is_available_false(self):
        self.product.remove_from_stock(10)
        self.assertFalse(self.product.is_available())

if __name__ == '__main__':
    unittest.main()
