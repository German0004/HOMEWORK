# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.


# Створення списку цілих чисел
numbers = list(range(1, 21))  # Наприклад, список від 1 до 20

# Отримання списку квадратів непарних чисел
squares_of_odd_numbers = [x**2 for x in numbers if x % 2 != 0]

print("Список цілих чисел:", numbers)
print("Список квадратів непарних чисел:", squares_of_odd_numbers)


Пояснення коду:
Створення списку цілих чисел: numbers = list(range(1, 21)) створює список чисел від 1 до 20.
Отримання списку квадратів непарних чисел: squares_of_odd_numbers = [x**2 for x in numbers if x % 2 != 0] використовує генератор списків для створення нового списку, який містить квадрати чисел з вихідного списку numbers, якщо ці числа непарні (тобто x % 2 != 0).
Виведення результатів: print використовується для виведення вихідного списку цілих чисел і списку квадратів непарних чисел.