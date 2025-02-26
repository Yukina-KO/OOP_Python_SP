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
        self.products: list = products

        Category.category_count += 1
        Category.product_count = len(self.products)
```

#### Описание:
- Отвечает за хранение информации о категории товаров.
- Поля:
  - `name` (str) - название категории.
  - `description` (str) - описание категории.
  - `products` (list) - список товаров в категории.
- Статические переменные:
  - `category_count` - счётчик категорий.
  - `product_count` - количество товаров в последней созданной категории.

---

### 2. Класс `Product`

**Файл:** `src/Classes/Product/product.py`

```python
class Product:
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

        Product.product_count += 1
```

#### Описание:
- Отвечает за хранение информации о конкретном продукте.
- Поля:
  - `name` (str) - название продукта.
  - `description` (str) - описание продукта.
  - `price` (float) - цена продукта.
  - `quantity` (int) - количество единиц продукта на складе.
- Статическая переменная:
  - `product_count` - счётчик созданных объектов `Product`.

## Тесты

### 1. Тесты для `Category`

**Файл:** `tests/test_category.py`

```python
from src.Classes.Category.category import Category
from src.Classes.Product.product import Product

def test_category_creation() -> None:
    product1 = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product2 = Product("Monitor", "4K Ultra HD Monitor", 299.99, 3)
    category = Category("Electronics", "Devices and gadgets", [product1, product2])

    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert len(category.products) == 2
    assert category.products[0].name == "Tablet"
    assert category.products[1].name == "Monitor"

def test_category_count_increment() -> None:
    initial_category_count = Category.category_count
    Category("Appliances", "Home appliances", [])
    assert Category.category_count == initial_category_count + 1

def test_category_product_count() -> None:
    product1 = Product("Camera", "DSLR Camera", 799.99, 2)
    product2 = Product("Headphones", "Noise-canceling headphones", 199.99, 8)
    Category("Gadgets", "Wearable and portable devices", [product1, product2])
    assert Category.product_count == 2
```

### 2. Тесты для `Product`

**Файл:** `tests/test_products.py`

```python
from src.Classes.Product.product import Product

def test_product_creation() -> None:
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)

    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10

def test_product_count_increment() -> None:
    initial_count = Product.product_count
    Product("Phone", "Latest model smartphone", 999.99, 5)
    assert Product.product_count == initial_count + 1
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```sh
pytest tests/
```

Это выполнит все тесты, находящиеся в каталоге `tests/`.
