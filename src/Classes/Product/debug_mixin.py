class DebugMixin:
    def __init__(self, *args, **kwargs) -> None:
        # Формируем строку с параметрами
        class_name = self.__class__.__name__
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        params = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Создан объект класса {class_name} с параметрами: ({params})")
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"
