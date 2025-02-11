if __name__ == "__main__":
    # Write your solution here
    class Animal:
        """
        Базовый класс животных.

        Атрибуты:
            name (str): Имя животного.
            age (int): Возраст животного (в годах).
        """

        def __init__(self, name: str, age: int) -> None:
            """
            Инициализация животного.

            Аргументы:
                name (str): Имя животного.
                age (int): Возраст животного.
            """
            self._name = name
            self._age = age

        def __str__(self) -> str:
            """Возвращает строковое представление животного."""
            return f"{self.__class__.__name__}(Имя: {self._name}, Возраст: {self._age})"

        def __repr__(self) -> str:
            """Возвращает формальное строковое представление животного."""
            return f"{self.__class__.__name__}(name={self._name!r}, age={self._age!r})"

        def sound(self) -> str:
            """Метод, описывающий звук, который издает животное."""
            return "Звук"


    class Dog(Animal):
        """
        Класс собаки, наследующий от Animal.

        Атрибуты:
            breed (str): Порода собаки.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Инициализация собаки.

            Аргументы:
                name (str): Имя собаки.
                age (int): Возраст собаки.
                breed (str): Порода собаки.
            """
            super().__init__(name, age)
            self.breed = breed

        def __str__(self) -> str:
            """Возвращает строковое представление собаки."""
            return f"{super().__str__()}, Порода: {self.breed}"

        def sound(self) -> str:
            """Перегруженный метод, описывающий звук, который издает собака.

            Возвращает:
                str: Звук, который издает собака.

            Обоснование:
                Собака лает, и это является характерным звуком для этого вида животных.
            """
            return "Гав!"



    class Cat(Animal):
        """
        Класс кошки, наследующий от Animal.

        Атрибуты:
            color (str): Цвет кошки.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            Инициализация кошки.

            Аргументы:
                name (str): Имя кошки.
                age (int): Возраст кошки.
                color (str): Цвет кошки.
            """
            super().__init__(name, age)
            self.color = color

        def __str__(self) -> str:
            """Возвращает строковое представление кошки."""
            return f"{super().__str__()}, Цвет: {self.color}"

        def sound(self) -> str:
            """Перегруженный метод, описывающий звук, который издает кошка.

            Возвращает:
                str: Звук, который издает кошка.

            Обоснование:
                Кошка мяукает, и это является характерным звуком для этого вида животных.
            """
            return "Мяу!"

#Пример реализации
    if __name__ == "__main__":
        dog = Dog(name="Бублик", age=3, breed="Немецкий дог")
        cat = Cat(name="Вискас", age=2, color="Белый")

        print(dog)
        print(cat)

        print(dog.sound())
        print(cat.sound())
    pass
