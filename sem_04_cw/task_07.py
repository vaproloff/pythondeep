# Задание No7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами
# (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
# а если хотя бы одна убыточная — ложь.


def analyse_comp(data: dict[str, list[int]]) -> bool:
    # for money_flows in companies.values():
    #     if sum(money_flows) < 0:
    #         return False
    # return True
    return all(map(lambda x: sum(x) > 0, data.values()))


companies = {
    'samsung': [100, -300, 1200, 500],
    'google': [357, 677, -350, -500, 100],
    'apple': [-900, -300, 447, 3000],
    'haier': [1000, -3300, 7200, -5500],
    'panasonic': [3467, -39999, 34550, 3456],
}
print(analyse_comp(companies))
