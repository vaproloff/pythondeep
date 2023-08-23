# Задание No4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответствует формату.

from datetime import datetime
import logging

logging.basicConfig(filename='task_04.log', filemode='a', level=logging.ERROR, encoding='utf-8')
logger = logging.getLogger(__name__)

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')


def get_date(input_date: str) -> datetime | None:
    try:
        day_count, weekday, month = input_date.split()
    except ValueError as e:
        logger.error(f'String {input_date} can\'t be splitted. ({e})')
        return None
    day_count = int(day_count[0])
    weekday = WEEKDAYS.index(weekday[:3])
    month = MONTHS.index(month[:3]) + 1
    i = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == weekday:
            i += 1
        if i == day_count:
            return date


if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
