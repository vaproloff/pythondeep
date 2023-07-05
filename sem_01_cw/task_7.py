MIN_SINGLE_NUM = 1
MAX_SINGLE_NUM = 9
MIN_TRIPLE_NUM = 100
MAX_TRIPLE_NUM = 999

num = 0
result = 0

while not (MIN_SINGLE_NUM <= num <= MAX_TRIPLE_NUM):
    num = int(input('Введите число: '))

if num <= MAX_SINGLE_NUM:
    result = num ** 2
elif MAX_SINGLE_NUM < num < MIN_TRIPLE_NUM:
    result = (num // 10) * (num % 10)
else:
    result = num // 100 + ((num // 10) % 10) * 10 + (num % 10) * 100

print(result)
