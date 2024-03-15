class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Марка: {self.brand}, год выпуска: {self.year}"


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        return f"Автомобиль: {self.brand} {self.model}, год выпуска: {self.year}"


# Функция для создания объекта Car с обработкой исключений
def create_car(brand, year, model):
    try:
        if not isinstance(year, int) or year < 1900 or year > 2022:
            raise ValueError("Неверный год выпуска")
        car = Car(brand, year, model)
        return car
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None


# Создание объектов класса Car с проверкой на ошибки
car1 = create_car("Toyota", 2018, "Camry")
car2 = create_car("Honda", "2020", "Civic")
car3 = create_car("Ford", 2015, "Mustang")

# Вывод информации о каждом автомобиле
if car1:
    print(car1.display_info())
if car2:
    print(car2.display_info())
if car3:
    print(car3.display_info())
