# Нехай на кожну сходинку можна стати з попередньої або переступивши через одну. Визначте, скількома способами можна
# піднятися на задану сходинку.

# Це класична задача з теорії чисел, яка описується послідовністю Фібоначчі. Щоб піднятися на задану сходинку n, кількість
# способів, якими це можна зробити, відповідає F(n+1), де F(n) — це n-е число Фібоначчі.
# Пояснення:
# •	Якщо ми знаходимося на сходинці n, то на неї можна потрапити з попередньої сходинки (n−1) або перестрибнути
# через одну (n-2).
# •	Таким чином, кількість способів піднятися на nnn-у сходинку дорівнює сумі кількості способів піднятися на n−1 і
# на n−2 сходинки.
# •	Це саме визначення чисел Фібоначчі: F(n)=F(n−1)+F(n−2).
# Формально, для підйому на nnn-у сходинку, кількість способів визначається як F(n+1)F(n+1)F(n+1), де:
# •	F(0)=0
# •	F(1)=1
# •	F(n)=F(n−1)+F(n−2) для n≥2n


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def ways_to_climb(n):
    return fibonacci(n + 1)


# Приклади
n = 5
print(f"Кількість способів піднятися на {n}-у сходинку: {ways_to_climb(n)}")

n = 9
print(f"Кількість способів піднятися на {n}-у сходинку: {ways_to_climb(n)}")


# У цьому коді функція fibonacci обчислює n-е число Фібоначчі, а ways_to_climb визначає кількість способів піднятися
# на задану сходинку 𝑛