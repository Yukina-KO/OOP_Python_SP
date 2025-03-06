# README

## Проект "OOP_Python_SP"

Данный проект реализует три основные сущности: **Category** (Категория), **Product** (Продукт) и **CategoryIterator** (Итератор категории). В дополнение к базовому классу `Product`, добавлены специализированные классы **Smartphone** (Смартфон) и **LawnGrass** (Газонная трава). Также присутствуют тесты, проверяющие их корректность.

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
│       │   ├── product.py
│       │   ├── smartphone.py
│       │   ├── lawn_grass.py
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

Класс `Category` отвечает за управление категориями товаров.

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

Класс `Product` реализует базовую логику товаров.

```python
class Product:
    ...  # Основная реализация класса
```

### 4. Класс `Smartphone`

**Файл:** `src/Classes/Product/smartphone.py`

```python
from .product import Product

class Smartphone(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.model}, {self.memory}GB, {self.color}), {self.price} руб. Остаток: {self.quantity} шт."
```

### 5. Класс `LawnGrass`

**Файл:** `src/Classes/Product/lawn_grass.py`

```python
from .product import Product

class LawnGrass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.country}, {self.color}), {self.price} руб. Остаток: {self.quantity} шт."
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```sh
pytest tests/
```
