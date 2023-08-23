# Задание No5
# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить.
#    В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
#
# 📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='task_04.log', filemode='a', level=logging.ERROR, encoding='utf-8')
logger = logging.getLogger(__name__)

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')


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


def parse():
    parser = argparse.ArgumentParser(prog='get_data',
                                     description='Get datetime object from input string',
                                     epilog='get_date("1-й четверг ноября")')
    parser.add_argument('-c', '--count', default='1', help='Какой по счёту день недели')
    parser.add_argument('-w', '--weekday', default=WEEKDAYS[datetime.now().weekday()], help='День недели')
    parser.add_argument('-m', '--month', default=MONTHS[datetime.now().month], help='Месяц')
    args = parser.parse_args()
    return get_date(f'{args.count} {args.weekday}, {args.month}')


if __name__ == '__main__':
    print(parse())
