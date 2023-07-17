# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import datetime
import decimal

START_STORE = decimal.Decimal(0.0)
OPERATION_DIVIDER = 50
WITHDRAW_TAX = 1.5
MIN_WITHDRAW_TAX = 30
MAX_WITHDRAW_TAX = 600
LOYALTY_RATE = 3
LOYALTY_PERIOD = 3
WEALTH_TAX = 10
WEALTH_LIMIT = 5_000_000


def collect_wealth_tax(total: decimal.Decimal, wealth_limit: int, tax: float) -> decimal.Decimal | None:
    if total > wealth_limit:
        return -total * decimal.Decimal(tax) / 100


def deposit(divider: int) -> decimal.Decimal | None:
    deposit_amount = decimal.Decimal(input('Сумма пополнения: '))
    if deposit_amount > 0 and deposit_amount % divider == 0:
        return +deposit_amount
    else:
        print(f'Сумма должна быть кратной {divider} у.е.!')


def withdraw(total: decimal.Decimal, divider: int, tax_rate: float, min_tax: int, max_tax: int)\
            -> decimal.Decimal | None:
    withdraw_amount = decimal.Decimal(input('Сумма снятия: '))
    if withdraw_amount > 0 and withdraw_amount % divider == 0:
        withdraw_tax = withdraw_amount * decimal.Decimal(tax_rate) / 100
        if min_tax < withdraw_tax < max_tax:
            withdraw_amount += withdraw_tax
        elif withdraw_tax < min_tax:
            withdraw_amount += min_tax
        else:
            withdraw_amount += max_tax

        if withdraw_amount > total:
            print('Сумма превышает остаток ня счёте!')
        else:
            return -withdraw_amount
    else:
        print(f'Сумма должна быть кратной {divider} у.е.!')


def add_loyalty_dividends(total: decimal.Decimal, operation: int, rate: float, period: int) -> decimal.Decimal | None:
    if operation % period == 0:
        return +total * decimal.Decimal(rate) / 100


def process_operation(total: decimal.Decimal, amount: decimal.Decimal, operation: str,
                      log: list[dict[str, int | float | str]]) -> decimal.Decimal:
    if amount:
        log.append({
            'datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'operation': operation,
            'amount': amount
        })
        return total + decimal.Decimal(amount)
    return total


def run(store: decimal.Decimal, log: list[dict[str, int | float | str]]):
    print('Добро пожаловать в банкомат!')

    while True:
        store = process_operation(store, collect_wealth_tax(store, WEALTH_LIMIT, WEALTH_TAX), 'wealth tax', log)

        action = input('------------------\n'
                       f'На Вашем счёте {round(store, 2)} у.е.\nЧто Вы хотите сделать?\n'
                       '1 - Пополнить. 2 - Снять. 3 - История операций. 0 - Выйти.\n'
                       'Выбор: ')
        match action:
            case '1':
                store = process_operation(store, deposit(OPERATION_DIVIDER), 'deposit', log)
            case '2':
                store = process_operation(store, withdraw(store, OPERATION_DIVIDER, WITHDRAW_TAX, MIN_WITHDRAW_TAX,
                                                          MAX_WITHDRAW_TAX), 'withdrawal', log)
            case '3':
                print('\n'.join(map(str, log)))
            case _:
                exit(0)

        store = process_operation(store, add_loyalty_dividends(store, len(log), LOYALTY_RATE, LOYALTY_PERIOD),
                                  'loyalty dividends', log)


run(START_STORE, list())
