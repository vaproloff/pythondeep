text = input('Введите текст: ')
if text.isdigit():
    num = int(text)
    print(bin(num), oct(num), hex(num))
elif text.isascii():
    print('Текст написан в ASCII')
else:
    print('Текст написан не в ASCII')
