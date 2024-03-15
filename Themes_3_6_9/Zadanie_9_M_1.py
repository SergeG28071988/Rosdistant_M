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
    # Соединение данных один-ко-многим
    for electro_car in electro_cars:
        for owner in owners:
            if owner.id == electro_car.owner_id:
                print(f"Электрокар {electro_car.brand} принадлежит владельцу {owner.fio}")

    # Соединение данных многие ко многим-ко-многим
    for owner in owners:
        owned_electro_cars = [electro_car.brand for electro_car in electro_cars if any(owner.id == eo.owner_id for eo in owner_electro)]
        owned_classic_cars = [classic_car.brand for classic_car in classic_cars if any(owner.id == co.owner_id for co in owner_classic)]
        print(f"{owner.fio} владеет электрокарами: {', '.join(owned_electro_cars)} и классическими автомобилями: {', '.join(owned_classic_cars)}")

    # Задание 1
    sorted_electro_cars = sorted(electro_cars, key=itemgetter('owner_id'))
    print("\nСортировка электрокаров по владельцам:")
    for electro_car in sorted_electro_cars:
        owner = next(owner for owner in owners if owner.id == electro_car.owner_id)
        print(f"{electro_car.brand} принадлежит {owner.fio}")

    # Задание 2
    car_prices = {}
    for owner in owners:
        total_price = sum(car.price for car in electro_cars + classic_cars if any(owner.id == eo.owner_id or owner.id == co.owner_id for eo in owner_electro for co in owner_classic))
        car_prices[owner.fio] = total_price

    sorted_prices = dict(sorted(car_prices.items(), key=lambda x: x[1]))
    print("\nСуммарная стоимость автомобилей у владельцев:")
    for owner, price in sorted_prices.items():
        print(f"{owner}: {price}")

    # Задание 3
    car_owners_dict = {}
    for car in electro_cars + classic_cars:
        owner = next(owner.fio for owner in owners if owner.id == car.owner_id)
        if car.brand not in car_owners_dict:
            car_owners_dict[car.brand] = [owner]
        else:
            car_owners_dict[car.brand].append(owner)

    print("\nСловарь автовладельцев по маркам автомобилей:")
    for car, owners_list in car_owners_dict.items():
        print(f"{car}: {', '.join(owners_list)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Произошла ошибка: {e}")


