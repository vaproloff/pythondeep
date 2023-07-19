# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibo_gen(n: int):
    prev = 0
    cur = 1
    for _ in range(n):
        yield cur
        prev, cur = cur, prev + cur


print(*fibo_gen(20))
