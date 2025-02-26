from typing import Dict, List, Optional, Union


class Product:
    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity

        Product.product_count += 1

    @property
    def price(self) -> float:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для установки новой цены.
        Если цена меньше или равна 0 – выводим сообщение об ошибке.
        Если новая цена ниже текущей, запрашиваем подтверждение у пользователя.
        """
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
        """
        Класс-метод для создания нового товара.
        При наличии duplicates_list ищется товар с таким же именем.
        Если найден дубликат, то количество суммируется, а цена становится максимальной.
        Если duplicates_list не передан или дубликат не найден, создается новый объект.
        """
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
