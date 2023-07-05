GREGORIAN_YEAR = 1582
MULTI_4 = 4
MULTI_100 = 100
MULTI_400 = 400
YEAR_YES = '{} - високосный год'
YEAR_NO = '{} - невисокосный год'
YEAR_BEFORE = '{} - год не в грегорианском календаре'

year = int(input('Введите год: '))
result = ''
if year <= GREGORIAN_YEAR:
    result = YEAR_BEFORE.format(year)
elif year % MULTI_400 == 0:
    result = YEAR_YES.format(year)
elif year % MULTI_100 == 0:
    result = YEAR_NO.format(year)
elif year % MULTI_4 == 0:
    result = YEAR_YES.format(year)
else:
    result = YEAR_NO.format(year)

print(result)
