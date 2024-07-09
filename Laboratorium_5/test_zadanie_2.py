# -*- coding: utf-8 -*-
import pytest
from zadanie_1_class import Product

@pytest.fixture
def product():
    return Product("Test Product", 50, 10)

@pytest.mark.add_to_stock
def test_add_to_stock(product):
    product.add_to_stock(5)
    assert product.quantity == 15

@pytest.mark.remove_from_stock
def test_remove_from_stock(product):
    product.remove_from_stock(3)
    assert product.quantity == 7

@pytest.mark.remove_from_stock
def test_remove_from_stock_insufficient_quantity(product):
    with pytest.raises(ValueError):
        product.remove_from_stock(15)

@pytest.mark.parametrize("quantity", [0, -5])
@pytest.mark.add_to_stock
def test_invalid_quantity_add_to_stock(product, quantity):
    with pytest.raises(ValueError):
        product.add_to_stock(quantity)

@pytest.mark.parametrize("quantity", [0, -5])
@pytest.mark.remove_from_stock
def test_invalid_quantity_remove_from_stock(product, quantity):
    with pytest.raises(ValueError):
        product.remove_from_stock(quantity)

@pytest.mark.is_available
def test_is_available(product):
    assert product.is_available() is True

@pytest.mark.is_available
def test_is_available_empty_stock():
    empty_product = Product("Empty Product", 100, 0)
    assert empty_product.is_available() is False
