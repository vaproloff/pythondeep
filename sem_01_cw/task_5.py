n = int(input('Введите целое число: '))
e = int(input('Введите число кратности: '))

num_sum = 0
i = 1
while i <= n:
    if i % 2 == 0 and i % e != 0:
        num_sum += i
    i += 1
print(num_sum)
