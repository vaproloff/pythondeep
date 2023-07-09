# Задание No6.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

WEALTH_TAX = 10
WEALTH_LIMIT = 5_000_000
OPERATION_DIVIDER = 50
WITHDRAW_TAX = 1.5
LOYALTY_DIVIDENDS = 3
LOYALTY_PERIOD = 3
MIN_WITHDRAW_TAX = 30
MAX_WITHDRAW_TAX = 600

cash_store = 0.0
operation = 1

print('Добро пожаловать в банкомат!')
while True:
    if cash_store > WEALTH_LIMIT:
        cash_store *= (100 - WEALTH_TAX) / 100

    print(f'На Вашем счёте {cash_store} у.е.')

    action = input('Что Вы хотите сделать?\n'
                   '1 - Пополнить. 2 - Снять. 0 - Выйти.\n'
                   'Выбор: ')

    match action:
        case '0':
            exit(0)

        case '1':
            cash_added = int(input('Сумма пополнения: '))
            if cash_added < 0:
                print('Сумма не может быть отрицательной!')
            elif cash_added % OPERATION_DIVIDER == 0:
                cash_store += cash_added
            else:
                print(f'Сумма должна быть кратной {OPERATION_DIVIDER} у.е.!')

        case '2':
            cash_withdraw = int(input('Сумма снятия: '))
            if cash_withdraw < 0:
                print('Сумма не может быть отрицательной!')
            elif cash_withdraw % OPERATION_DIVIDER == 0:
                withdraw_tax = cash_withdraw * WITHDRAW_TAX / 100
                if MIN_WITHDRAW_TAX < withdraw_tax < MAX_WITHDRAW_TAX:
                    cash_withdraw += withdraw_tax
                elif withdraw_tax < MIN_WITHDRAW_TAX:
                    cash_withdraw += MIN_WITHDRAW_TAX
                else:
                    cash_withdraw += MAX_WITHDRAW_TAX
                if cash_withdraw > cash_store:
                    print('Сумма превышает остаток ня счёте!')
                else:
                    cash_store -= cash_withdraw
            else:
                print(f'Сумма должна быть кратной {OPERATION_DIVIDER} у.е.!')

    if operation % LOYALTY_PERIOD == 0:
        cash_store *= (100 + LOYALTY_DIVIDENDS) / 100
    operation += 1
