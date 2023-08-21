import doctest


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    """
    Checks if input string date is valid
    >>> check_date('01.01.2000')
    True
    >>> check_date('29.02.2000')
    True
    >>> check_date('29.02.2001')
    False
    >>> check_date('40.01.2000')
    False
    >>> check_date('31.04.2000')
    False
    >>> check_date('31.05.2000')
    True
    >>> check_date('10.13.2000')
    False
    """
    day, month, year = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and if_leap(year) and day > 29:
        return False

    if month == 2 and not if_leap(year) and day > 28:
        return False

    return True


if __name__ == '__main__':
    doctest.testmod(verbose=True)
