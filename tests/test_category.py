import pytest

from src.Classes.Category.category import Category
from src.Classes.Product.product import Product
from src.Classes.Product.smartphone import Smartphone
from src.Classes.Product.lawn_grass import LawnGrass


def test_category_creation() -> None:
    product1 = Product("Monitor", "4K Ultra HD Monitor", 299.99, 3)
    product2 = Product("Mouse", "Wireless Mouse", 29.99, 10)
    category = Category("Electronics", "Devices and gadgets", [product1, product2])
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert Category.product_count == 2


def test_category_add_product() -> None:
    product = Product("Keyboard", "Mechanical keyboard", 99.99, 4)
    category = Category("Accessories", "Computer accessories", [])
    category.add_product(product)
    assert Category.product_count == 1


def test_category_products_format() -> None:
    product1 = Product("Smartwatch", "Fitness tracking watch", 199.99, 5)
    product2 = Product("Headphones", "Noise-canceling headphones", 149.99, 8)
    category = Category("Wearables", "Wearable tech devices", [product1, product2])
    expected_output = "Smartwatch, 199.99 руб. Остаток: 5 шт.\nHeadphones, 149.99 руб. Остаток: 8 шт."
    assert category.products == expected_output


def test_category_str() -> None:
    product1 = Product("Item1", "Desc1", 100, 5)
    product2 = Product("Item2", "Desc2", 200, 3)
    category = Category("TestCat", "Test Desc", [product1, product2])
    assert str(category) == "TestCat, количество продуктов: 8 шт."


def test_category_iteration() -> None:
    product1 = Product("Item1", "Desc1", 100, 5)
    product2 = Product("Item2", "Desc2", 200, 3)
    category = Category("TestCat", "Test Desc", [product1, product2])
    products = list(category)
    assert len(products) == 2
    assert products[0].name == "Item1"
    assert products[1].name == "Item2"


def test_add_product_valid() -> None:
    category = Category("Test", "Test desc", [])
    product = Product("TestItem", "Test desc", 50.0, 2)
    smartphone = Smartphone("Phone", "Smartphone", 1000, 5, 2.5, "X1", 128, "Black")
    grass = LawnGrass("Grass", "Green grass", 50, 20, "Russia", "10-14 дней", "Green")
    category.add_product(product)
    category.add_product(smartphone)
    category.add_product(grass)
    assert len(category.get_products()) == 3


def test_add_product_invalid() -> None:
    category = Category("Test", "Test desc", [])
    with pytest.raises(TypeError):
        category.add_product("not_a_product")
