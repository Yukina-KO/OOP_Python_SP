# README

## Проект "OOP_Python_SP"

Данный проект реализует две основные сущности: **Category** (Категория) и **Product** (Продукт). Также присутствуют тесты, проверяющие их корректность.

## Структура проекта

```
OOP_Python_SP/
│── data/
│   └── products.json
│── src/
│   └── Classes/
│       ├── Category/
│       │   ├── __init__.py
│       │   └── category.py
│       ├── Product/
│       │   ├── __init__.py
│       │   └── product.py
│── tests/
│   ├── __init__.py
│   ├── test_category.py
│   ├── test_products.py
│── main.py
│── poetry.lock
│── pyproject.toml
```

## Классы

### 1. Класс `Category`

**Файл:** `src/Classes/Category/category.py`

```python
class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.__products: list = products

        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self):
        lines = []
        for prod in self.__products:
            line = f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            lines.append(line)
        return "\n".join(lines)
```

### 2. Класс `Product`

**Файл:** `src/Classes/Product/product.py`

```python
class Product:
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity

        Product.product_count += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if answer.lower() != "y":
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_info: dict, duplicates_list: list = None):
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")

        if duplicates_list is not None:
            for prod in duplicates_list:
                if prod.name == name:
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.price = price
                    return prod

        return cls(name, description, price, quantity)
```

## Тесты

### 1. Тесты для `Category`

**Файл:** `tests/test_category.py`

```python
from src.Classes.Product.product import Product
from src.Classes.Category.category import Category

def test_category_creation():
    product1 = Product("Monitor", "4K Ultra HD Monitor", 299.99, 3)
    product2 = Product("Mouse", "Wireless Mouse", 29.99, 10)
    category = Category("Electronics", "Devices and gadgets", [product1, product2])

    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert Category.product_count == 2

def test_category_add_product():
    product = Product("Keyboard", "Mechanical keyboard", 99.99, 4)
    category = Category("Accessories", "Computer accessories", [])
    category.add_product(product)
    assert Category.product_count == 1

def test_category_products_format():
    product1 = Product("Smartwatch", "Fitness tracking watch", 199.99, 5)
    product2 = Product("Headphones", "Noise-canceling headphones", 149.99, 8)
    category = Category("Wearables", "Wearable tech devices", [product1, product2])
    expected_output = "Smartwatch, 199.99 руб. Остаток: 5 шт.\nHeadphones, 149.99 руб. Остаток: 8 шт."
    assert category.products == expected_output
```

### 2. Тесты для `Product`

**Файл:** `tests/test_products.py`

```python
from src.Classes.Product.product import Product

def test_product_creation():
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10

def test_product_price_setter():
    product = Product("Phone", "Latest model smartphone", 999.99, 5)
    product.price = 1200.00
    assert product.price == 1200.00

def test_product_price_negative():
    product = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product.price = -50
    assert product.price == 499.99

def test_new_product_with_duplicates():
    product1 = Product("Camera", "DSLR Camera", 800, 2)
    duplicates = [product1]
    new_product = Product.new_product({"name": "Camera", "description": "DSLR Camera", "price": 750, "quantity": 3}, duplicates)
    assert new_product.quantity == 5
    assert new_product.price == 800
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```sh
pytest tests/
```
