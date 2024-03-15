# используется для сортировки
from operator import itemgetter


class Car:
    """Автомобиль"""

    def __init__(self, id, brand, year, price, owner_id):
        self.id = id
        self.brand = brand
        self.year = year
        self.price = price
        self.owner_id = owner_id


class ElectroCar(Car):
    """Электрокар"""
    pass


class ClassicCar(Car):
    """Классический автомобиль"""
    pass


class Owner:
    """Владелец"""

    def __init__(self, id, fio):
        self.id = id
        self.fio = fio


class ElectroCarOwner:
    """ Электро-автомобили для реализации связи многие ко многим """

    def __init__(self, owner_id, car_id):
        self.owner_id = owner_id
        self.car_id = car_id


class ClassicCarOwner:
    """ Классические автомобили для реализации связи многие ко многим """

    def __init__(self, owner_id, car_id):
        self.owner_id = owner_id
        self.car_id = car_id


# Автовладельцы
owners = [
    Owner(1, 'Иванов Иван Иванович'),
    Owner(2, 'Петров Петр Петрович'),
    Owner(3, 'Сидоров Сидор Сидорович')
]

# Электрокары
electro_cars = [
    ElectroCar(1, 'Tesla', 2021, 50000, 1),
    ElectroCar(2, 'Nissan', 2020, 40000, 2),
    ElectroCar(3, 'BMW', 2019, 60000, 3)
]

# Классические автомобили
classic_cars = [
    ClassicCar(4, 'Ford', 2015, 30000, 1),
    ClassicCar(5, 'Chevrolet', 2018, 35000, 2),
    ClassicCar(6, 'Mercedes', 2017, 45000, 3)
]

# Связь между владельцами и электрокарами
owner_electro = [
    ElectroCarOwner(1, 1),
    ElectroCarOwner(2, 2),
    ElectroCarOwner(3, 3)
]

# Связь между владельцами и классическими автомобилями
owner_classic = [
    ClassicCarOwner(1, 4),
    ClassicCarOwner(2, 5),
    ClassicCarOwner(3, 6)
]


# Основная функция программы
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    " ...... код......  "

    # Соединение данных многие ко многим-ко-многим
    " ...... код......  "

    # Задание 1
    # Выполнить сортировку по связи один-ко-многим
    " ...... код......  "

    # Задание 2
    # Перебрать всех автовладельцев, вывести стоимость автомобиля и суммарную стоимость
    # Выполнить сортировку по суммарной стоимости автомобиля
    " ...... код......  "

    # Задание 3
    # Перебрать всех автовладельцев, вывести фамилии, добавить результат в словарь.
    # Ключ - автомобиль, значение - список фамилий
    # Выполнить сортировку суммарной стоимости автомобиля
    " ...... код......  "

    # также нужно добавить проверку на ошибки - try except


if __name__ == '__main__':
    main()
