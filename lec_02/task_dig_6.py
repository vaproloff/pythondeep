DEFAULT = 42
num = int(input('введите уровень или ноль для значения по умолчанию: '))
level = num or DEFAULT
print(level)
