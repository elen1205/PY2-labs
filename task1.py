import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Furniture:
    def __init__(self, material: str, weight: float, location: str):
        """
    Инициализация объекта Furniture.
    :param material: Материал мебели (должен быть строкой)
    :param weight: Вес мебели в кг (должен быть положительным числом)
    : raises ValueError: if weight <= 0
    :param location: Местоположение мебели (должен быть строкой)
    """
        if not isinstance(material, str) or not isinstance(location, str):
            raise TypeError("Материал и местоположение дожны быть строками")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        self.material = material
        self.weight = weight
        self.location = location

    def assemble(self) -> None:
        """
    Метод для сборки мебели.
    :return: None
    """
    ...

    def disassemble(self) -> None:
        """
    Метод для разборки мебели.
    :return: None
    """
    ...

    def move(self, new_location: str) -> None:
        """
    Метод для перемещения мебели в новое место.

    :param new_location: Новое местоположение (должно быть строкой).
    :return: None
Примеры:
    >>> table = Furniture('белое дерево', 10.0, "Кухня")
    >>> table.move("Гостиница")
    """
    ...

class Vehicle:
    def __init__(self, company: str, model: str, year: int):
        """
        Создание объекта "Транспортное средство".

        :param company: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        :raises TypeError: Если company или model не строка, или year не целое число.
        :raises ValueError: Если year меньше 1886 (года появления первого автомобиля).
        """
        if not isinstance(company, str) or not isinstance(model, str):
            raise TypeError("Производитель и модель должны быть строками.")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")

        self.company = company
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """Запускает двигатель транспортного средства."""
        ...

    def beep_beep(self) -> None:
        """Сигналит гудком."""
        ...
    def get_model(self)-> str:
        """
        Возвращает модель машины.
        :return: Модель машины.
        Примеры:
        >>> vehicle =   Vehicle("Skoda", "Octavia", 2004)
        >>> vehicle.get_model()
        """

class Building:
    def __init__(self, address: str, floors: int):
        """
        Создание объекта "Здание".

        :param address: Адрес здания.
        :param floors: Количество этажей в здании.

        Примеры:
        >>> building = Building("ул. Пушкина 5", 5)

        :raises TypeError: Если address не строка или floors не целое число.
        :raises ValueError: Если floors меньше или равно нулю.
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой.")
        if not isinstance(floors, int):
            raise TypeError("Количество этажей должно быть целым числом.")
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом.")

        self.address = address
        self.floors = floors

    def open_doors(self) -> None:
        """Открывает двери здания."""
        ...

    def get_address(address) -> None:
        """Закрывает двери здания.
        Примеры:
        >>> building = Building("Екатерининская 6", 10)
        >>> building.get_address()
        """
        ...

    def get_floor_count(floors) -> int:
        """
        Возвращает количество этажей в здании.

        :return: Количество этажей.

        Примеры:
        >>> building = Building("Екатерининская 9", 10)
        >>> building.get_floor_count()
        """
        ...
if __name__ == "__main__":
   doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
pass