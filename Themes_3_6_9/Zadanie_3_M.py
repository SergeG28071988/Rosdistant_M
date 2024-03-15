def check_even_odd():
    try:
        num = int(input("Введите число: "))
        if num % 2 == 0:
            print("Четное")
        else:
            print("Нечетное")
    except ValueError:
        print("Ошибка: Введите целое число.")


if __name__ == "__main__":
    check_even_odd()
