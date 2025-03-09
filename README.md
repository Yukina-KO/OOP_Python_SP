# README

## Проект "OOP_Python_SP"

Данный проект реализует три основные сущности: **Category** (Категория), **Product** (Продукт) и **CategoryIterator** (Итератор категории). В дополнение к базовому классу `Product`, добавлены специализированные классы **Smartphone** (Смартфон) и **LawnGrass** (Газонная трава). Также реализован класс **Order** (Заказ) для управления заказами. Присутствуют тесты, проверяющие корректность работы всех классов.

## Структура проекта

```
OOP_Python_SP/
│── data/
│   └── products.json
│── src/
│   └── Classes/
│       ├── Category/
│       │   ├── init.py
│       │   ├── category.py
│       │   ├── category_iterator.py
│       ├── Order/
│       │   ├── init.py
│       │   ├── base_entity.py
│       │   ├── order.py
│       ├── Product/
│       │   ├── init.py
│       │   ├── base_product.py
│       │   ├── debug_mixin.py
│       │   ├── product.py
│       │   ├── smartphone.py
│       │   ├── lawn_grass.py
│── tests/
│   ├── init.py
│   ├── test_category.py
│   ├── test_order.py
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
from src.Classes.Order.base_entity import BaseEntity
from .category_iterator import CategoryIterator

class Category(BaseEntity):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        super().__init__(name, description)
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

    def __iter__(self) -> "CategoryIterator":
        return CategoryIterator(self)
```

### 2. Класс `CategoryIterator`

**Файл:** `src/Classes/Category/category_iterator.py`

Класс CategoryIterator используется для перебора продуктов в категории.

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

### 3. Класс `BaseEntity`

**Файл:** `src/Classes/Order/base_entity.py`

Абстрактный базовый класс BaseEntity для сущностей с общими атрибутами name и description.

```python
from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description

    @abstractmethod
    def __str__(self) -> str:
        pass
```

### 4. Класс `Order`

**Файл:** `src/Classes/Order/order.py`

Класс Order отвечает за управление заказами, включая информацию о продукте и итоговую стоимость.

```python
from src.Classes.Product.product import Product
from src.Classes.Order.base_entity import BaseEntity

class Order(BaseEntity):
    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ: {self.name}, Товар: {self.product.name}, " \
               f"Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
```

### 5. Класс `BaseProduct`

**Файл:** `src/Classes/Product/base_product.py`

Абстрактный базовый класс BaseProduct для продуктов, определяющий обязательные методы и свойства.

```python
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        pass
```

### 6. Класс `DebugMixin`

**Файл:** `src/Classes/Product/debug_mixin.py`

Миксин DebugMixin для отладки, выводит информацию о создании объектов.

```python
class DebugMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        params = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Создан объект класса {class_name} с параметрами: ({params})")
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"
```

### 7. Класс `Product`

**Файл:** `src/Classes/Product/product.py`

Класс `Product` реализует базовую логику товаров.

```python
from typing import Dict, List, Optional, Union
from .base_product import BaseProduct
from .debug_mixin import DebugMixin

class Product(DebugMixin, BaseProduct):
    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity
        Product.product_count += 1
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product или его наследников")
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного и того же класса")
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

    @classmethod
    def new_product(
        cls, product_info: Dict[str, Union[str, float, int]], duplicates_list: Optional[List["Product"]] = None
    ) -> "Product":
        name: str = product_info.get("name")  # type: ignore
        description: str = product_info.get("description")  # type: ignore
        price: float = product_info.get("price")  # type: ignore
        quantity: int = product_info.get("quantity")  # type: ignore

        if duplicates_list is not None:
            for prod in duplicates_list:
                if prod.name == name:
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.price = price
                    return prod

        return cls(name, description, price, quantity)
```

### 8. Класс `Smartphone`

**Файл:** `src/Classes/Product/smartphone.py`

Класс Smartphone наследуется от Product и добавляет специфические атрибуты для смартфонов.

```python
from .product import Product

class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.model}, {self.memory}GB, {self.color}), {self.price} руб. " \
               f"Остаток: {self.quantity} шт."
```

### 9. Класс `LawnGrass`

**Файл:** `src/Classes/Product/lawn_grass.py`

Класс LawnGrass наследуется от Product и добавляет специфические атрибуты для газонной травы.

```python
from .product import Product

class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.country}, {self.color}), {self.price} руб. Остаток: {self.quantity} шт."
```

## Тесты

### 1. Тесты для продуктов

**Файл:** `tests/test_products.py`

Проверяет корректность создания объектов Product, Smartphone, LawnGrass, а также работу методов и логики.

```python
import pytest
from src.Classes.Product.product import Product
from src.Classes.Product.smartphone import Smartphone
from src.Classes.Product.lawn_grass import LawnGrass

def test_product_creation(capsys) -> None:
    product = Product("Laptop", "A high-end gaming laptop", 1500.99, 10)
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 1500.99
    assert product.quantity == 10
    captured = capsys.readouterr()
    assert "Создан объект класса Product с параметрами: ('Laptop', 'A high-end gaming laptop', 1500.99, 10)" in captured.out

def test_product_price_setter() -> None:
    product = Product("Phone", "Latest model smartphone", 999.99, 5)
    product.price = 1200.00
    assert product.price == 1200.00

def test_product_price_negative(capsys) -> None:
    product = Product("Tablet", "A lightweight tablet", 499.99, 7)
    product.price = -50
    assert product.price == 499.99
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

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
    assert "Создан объект класса Smartphone с параметрами: ('Phone', 'Smartphone', 1000.0, 5, 2.5, 'X1', 128, 'Black')"

def test_lawn_grass_creation() -> None:
    grass = LawnGrass("Grass", "Green grass", 50.0, 20, "Russia", "10-14 дней", "Green")
    assert grass.name == "Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == "10-14 дней"
    assert grass.color == "Green"
    assert str(grass) == "Grass (Russia, Green), 50.0 руб. Остаток: 20 шт."
    assert "Создан объект класса LawnGrass с параметрами: " \
           "('Grass', 'Green grass', 50.0, 20, 'Russia', '10-14 дней', 'Green')"

def test_addition_same_class() -> None:
    smartphone1 = Smartphone("Phone1", "Desc", 1000, 2, 2.5, "X1", 128, "Black")
    smartphone2 = Smartphone("Phone2", "Desc", 2000, 3, 3.0, "X2", 256, "White")
    assert smartphone1 + smartphone2 == 8000

    grass1 = LawnGrass("Grass1", "Desc", 50, 10, "Russia", "10-14 дней", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 100, 5, "USA", "7-10 дней", "Dark Green")
    assert grass1 + grass2 == 1000

def test_addition_different_classes() -> None:
    smartphone = Smartphone("Phone", "Desc", 1000, 2, 2.5, "X1", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 50, 10, "Russia", "10-14 дней", "Green")
    with pytest.raises(TypeError):
        smartphone + grass
```

### 2. Тесты для заказов

**Файл:** `tests/test_order.py`

Проверяет корректность создания и работы с объектами Order.

```python
from src.Classes.Product.product import Product
from src.Classes.Order.order import Order

def test_order_creation() -> None:
    product = Product("Laptop", "Gaming laptop", 1500.0, 10)
    order = Order("Заказ 1", "Тестовый заказ", product, 2)
    assert order.name == "Заказ 1"
    assert order.description == "Тестовый заказ"
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 3000.0

def test_order_str() -> None:
    product = Product("Laptop", "Gaming laptop", 1500.0, 10)
    order = Order("Заказ 1", "Тестовый заказ", product, 2)
    assert str(order) == "Заказ: Заказ 1, Товар: Laptop, Количество: 2, Итоговая стоимость: 3000.0 руб."
```

### 3. Тесты для категорий

**Файл:** `tests/test_category.py`

Проверяет корректность работы с категориями товаров (оставлен без изменений, так как изменений не указано).

```python
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
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```sh
pytest tests/
```
