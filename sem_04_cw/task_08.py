# Задание No8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replace_to_none() -> None:
    global_vars = globals()
    res_dict = {}
    for key, value in global_vars.items():
        if key == 's':
            continue
        if key.endswith('s'):
            res_dict[key[:-1]] = value
            global_vars[key] = None
    for key, value in res_dict.items():
        global_vars[key] = value


nums = 123
s = 'er435'
names = ['fsf', 'dsad']
sabc = 'abc'

replace_to_none()
print(globals())
