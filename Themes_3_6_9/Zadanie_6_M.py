import random


def create_random_dict(size):
    my_dict = {}
    for _ in range(size):
        key = random.randint(1, 100)
        value = random.randint(1, 100)
        my_dict[key] = value
    return my_dict


def sort_dict_by_values(my_dict):
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    return sorted_dict


try:
    size = int(input("Введите размер словаря: "))
    if size <= 0:
        raise ValueError("Размер словаря должен быть положительным числом")

    my_dict = create_random_dict(size)
    print("Исходный словарь:")
    print(my_dict)

    sorted_dict = sort_dict_by_values(my_dict)
    print("Отсортированный словарь по значениям:")
    print(sorted_dict)

except ValueError as e:
    print(f"Ошибка: {e}. Пожалуйста, введите положительное целое число для размера словаря.")
