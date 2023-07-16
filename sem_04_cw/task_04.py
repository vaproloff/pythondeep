# Задание No4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


def sort_num(num_list: list[int]) -> list[int]:
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[i]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


nums = [10, 2, 45, 9, 2, 33, 80, 22, 5, 67, 5, 45]
print(sort_num(nums))
# print(nums)
