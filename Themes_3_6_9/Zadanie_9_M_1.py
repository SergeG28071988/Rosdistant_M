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


