data = ["один", "два", "три", "четыре", "пять", "шесть", "семь", ]
a, b, c, *d = data
print(f'{a = } {b = } {c = } {d = }')

a, b, *c, d = data
print(f'{a = } {b = } {c = } {d = }')

a, *b, c, d = data
print(f'{a = } {b = } {c = } {d = }')

*a, b, c, d = data
print(f'{a = } {b = } {c = } {d = }')
