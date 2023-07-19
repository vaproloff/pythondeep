# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Пётр', 'Василий', 'Иван']
wages = [15_000, 25_000, 35_000]
awards = ['7.5%', '10.25%', '6.75%']

# Вариант 1
awards_dict_1 = {names[i]: wages[i] * float(awards[i][:-1]) / 100 for i in range(len(names))}
print(awards_dict_1)

# Вариант 2
awards_dict_2 = {name: wage * float(award[:-1]) / 100 for name, wage, award in zip(names, wages, awards)}
print(awards_dict_2)
