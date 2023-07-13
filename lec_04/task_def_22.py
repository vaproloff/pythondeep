def main(a):
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }')
        return y + 1

    return x + func(a)


x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')
