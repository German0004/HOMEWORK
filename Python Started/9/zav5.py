# Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї функції створити змінні
# x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів) та функцію calc_rezult з формальними
# параметрами зовнішньої функції quadratic_equation. Всередині функції calc_rezult здійснити пошук дискримінанта,
# згідно з результатом якого зробити розрахунок коренів рівняння. Зовнішня функція quadratic_equation має повернути
# перелік значень коренів квадратного рівняння. Надати можливість користувачеві ввести з клавіатури формальні параметри
# для передачі їх у створену функцію quadratic_equation, результати роботи функції відобразити на екрані.


import math


def quadratic_equation(a, b, c):
    x1, x2 = None, None  # Початкове значення коренів, якщо ще не знайдені

    def calc_rezult(a, b, c):
        nonlocal x1, x2
        discriminant = b**2 - 4 * a * c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        elif discriminant == 0:
            x1 = x2 = -b / (2 * a)
        # Якщо дискримінант менше нуля, корені у вигляді комплексних чисел, їх не обчислюємо

    calc_rezult(a, b, c)
    return x1, x2


# Зчитуємо коефіцієнти a, b, c з клавіатури
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Обчислюємо корені квадратного рівняння
result = quadratic_equation(a, b, c)

# Виводимо результати
if result[0] is None:
    print("Квадратне рівняння не має реальних коренів.")
else:
    print("Корені квадратного рівняння:")
    print(f"x1 = {result[0]}")
    print(f"x2 = {result[1]}")


# Основні моменти цієї реалізації:
#
# Функція quadratic_equation приймає коефіцієнти a, b, c.
# Усередині quadratic_equation є внутрішня функція calc_rezult, яка обчислює корені за допомогою дискримінанта.
# Внутрішня функція calc_rezult має доступ до змінних x1 і x2 зовнішньої функції через ключове слово nonlocal.
# Результат виклику quadratic_equation містить корені рівняння у вигляді кортежу (x1, x2).
# Виведення результатів на екран залежить від того, чи знайдено реальні корені, чи рівняння не має реальних коренів
# (дискримінант менше нуля).


# Введіть коефіцієнт a: -2
# Введіть коефіцієнт b: 5
# Введіть коефіцієнт c: 5
# Корені квадратного рівняння:
# x1 = -0.7655644370746373
# x2 = 3.2655644370746373
