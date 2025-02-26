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
        """Сложение продуктов - возвращает общую стоимость всех товаров"""
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
