# Задание No7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def prime_gen_bad(n):
    count = 2
    while 1 < count <= n:
        is_simple = True
        for i in range(2, count // 2 + 1):
            if count % i == 0:
                count += 1
                is_simple = False
                break
        if is_simple:
            yield count
            count += 1


def prime_gen_good(n):
    for num in range(2, n + 1):
        is_simple = True
        for div in range(2, num // 2 + 1):
            if num % div == 0:
                is_simple = False
                break
        if is_simple:
            yield num


print(*prime_gen_bad(100))
print(*prime_gen_good(100))
