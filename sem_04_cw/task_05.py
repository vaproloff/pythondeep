# Задание No5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

import decimal


def get_awards(names: list[str], salaries: list[int], awards_pct: list[str]) -> dict[str: decimal.Decimal]:
    people_awards = {}
    for name, salary, award in zip(names, salaries, awards_pct):
        people_awards[name] = salary * decimal.Decimal(award[:-1]) / 100

    return people_awards


names = ['Петя', 'Вася', 'Ваня', 'Ирина']
salaries = [10_000, 25_000, 14_000, 17_500]
awards_pct = ['9.5%', '7.85%', '12.33%', '16.66%']

print(get_awards(names, salaries, awards_pct))
