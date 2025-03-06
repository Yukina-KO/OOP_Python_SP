import pytest

from src.Classes.Product.product import Product
from src.Classes.Product.smartphone import Smartphone
from src.Classes.Product.lawn_grass import LawnGrass


def test_product_creation() -> None:
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10


def test_product_price_setter() -> None:
    product = Product("Phone", "Latest model smartphone", 999.99, 5)
    product.price = 1200.00
    assert product.price == 1200.00


def test_product_price_negative() -> None:
    product = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product.price = -50
    assert product.price == 499.99


def test_new_product_with_duplicates() -> None:
    product1 = Product("Camera", "DSLR Camera", 800, 2)
    duplicates = [product1]
    new_product = Product.new_product(
        {"name": "Camera", "description": "DSLR Camera", "price": 750, "quantity": 3}, duplicates
    )
    assert new_product.quantity == 5
    assert new_product.price == 800


def test_product_str() -> None:
    product = Product("Monitor", "4K Monitor", 299.99, 3)
    assert str(product) == "Monitor, 299.99 руб. Остаток: 3 шт."


def test_product_addition() -> None:
    product1 = Product("Item1", "Desc1", 100, 10)
    product2 = Product("Item2", "Desc2", 200, 2)
    assert product1 + product2 == 1400


def test_smartphone_creation() -> None:
    smartphone = Smartphone("Phone", "Smartphone", 1000.0, 5, 2.5, "X1", 128, "Black")
    assert smartphone.name == "Phone"
    assert smartphone.efficiency == 2.5
    assert smartphone.model == "X1"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"
    assert str(smartphone) == "Phone (X1, 128GB, Black), 1000.0 руб. Остаток: 5 шт."


def test_lawn_grass_creation() -> None:
    grass = LawnGrass("Grass", "Green grass", 50.0, 20, "Russia", "10-14 дней", "Green")
    assert grass.name == "Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == "10-14 дней"
    assert grass.color == "Green"
    assert str(grass) == "Grass (Russia, Green), 50.0 руб. Остаток: 20 шт."


def test_addition_same_class() -> None:
    smartphone1 = Smartphone("Phone1", "Desc", 1000, 2, 2.5, "X1", 128, "Black")
    smartphone2 = Smartphone("Phone2", "Desc", 2000, 3, 3.0, "X2", 256, "White")
    assert smartphone1 + smartphone2 == 8000  # 1000*2 + 2000*3

    grass1 = LawnGrass("Grass1", "Desc", 50, 10, "Russia", "10-14 дней", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 100, 5, "USA", "7-10 дней", "Dark Green")
    assert grass1 + grass2 == 1000  # 50*10 + 100*5


def test_addition_different_classes() -> None:
    smartphone = Smartphone("Phone", "Desc", 1000, 2, 2.5, "X1", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 50, 10, "Russia", "10-14 дней", "Green")
    with pytest.raises(TypeError):
        smartphone + grass
