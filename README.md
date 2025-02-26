# README

## Проект "OOP_Python_SP"

Данный проект реализует три основные сущности: **Category** (Категория), **Product** (Продукт) и **CategoryIterator** (Итератор категории). Также присутствуют тесты, проверяющие их корректность.

## Структура проекта

```
OOP_Python_SP/
│── data/
│   └── products.json
│── src/
│   └── Classes/
│       ├── Category/
│       │   ├── __init__.py
│       │   ├── category.py
│       │   ├── category_iterator.py
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
from typing import List
from src.Classes.Product.product import Product
from .category_iterator import CategoryIterator

class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def get_products(self) -> List[Product]:
        return self.__products

    def __iter__(self):
        return CategoryIterator(self)
```

### 2. Класс `CategoryIterator`

**Файл:** `src/Classes/Category/category_iterator.py`

```python
from typing import List
from src.Classes.Product.product import Product

class CategoryIterator:
    def __init__(self, category: "Category") -> None:
        self.products: List[Product] = category.get_products()
        self.index: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> Product:
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product
```

### 3. Класс `Product`

**Файл:** `src/Classes/Product/product.py`

```python
from typing import Dict, List, Optional, Union

class Product:
    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity
        Product.product_count += 1

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer: str = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if answer.lower() != "y":
                return
        self.__price = new_price
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```sh
pytest tests/
```
