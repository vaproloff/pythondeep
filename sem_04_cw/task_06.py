# Задание No6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.


def get_sum_nums(num_list: list[int], start: int, end: int) -> int:
    i_start = max(0, min(start, end))
    i_end = min(len(num_list), max(start, end))
    return sum(num_list[i_start:i_end + 1])


nums = [10, 2, 45, 9, 2, 33, 80, 22, 5, 67, 5, 45]
print(get_sum_nums(nums, 5, 2))
