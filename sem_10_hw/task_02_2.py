import datetime
import decimal


class Atm:
    __operation_divider = 50
    __withdraw_tax_rate = 1.5
    __min_withdraw_tax_amount = 30
    __max_withdraw_tax_amount = 600
    __loyalty_rate = 2.5
    __loyalty_period = 5
    __wealth_tax_rate = 3
    __wealth_limit = 5_000_000

    def __init__(self, total_amount: decimal.Decimal = 0):
        self.__total_amount = total_amount
        self.__operation_count = 0
        self.__log = list()

    def __deposit(self):
        deposit_amount = decimal.Decimal(input('Сумма пополнения: '))
        if deposit_amount > 0 and deposit_amount % self.__operation_divider == 0:
            self.__total_amount += deposit_amount
            self.__add_to_log('deposit', deposit_amount)
        else:
            print(f'Сумма должна быть кратной {self.__operation_divider} у.е.!')

    def __withdraw(self):
        withdraw_amount = decimal.Decimal(input('Сумма снятия: '))
        if withdraw_amount > 0 and withdraw_amount % self.__operation_divider == 0:
            withdraw_tax = withdraw_amount * decimal.Decimal(self.__withdraw_tax_rate) / 100
            if self.__min_withdraw_tax_amount < withdraw_tax < self.__max_withdraw_tax_amount:
                withdraw_amount += withdraw_tax
            elif withdraw_tax < self.__min_withdraw_tax_amount:
                withdraw_amount += self.__min_withdraw_tax_amount
            else:
                withdraw_amount += self.__max_withdraw_tax_amount

            if withdraw_amount > self.__total_amount:
                print('Сумма превышает остаток ня счёте!')
            else:
                self.__total_amount -= withdraw_amount
                self.__add_to_log('withdrawal', withdraw_amount)
        else:
            print(f'Сумма должна быть кратной {self.__operation_divider} у.е.!')

    def __collect_wealth_tax(self):
        if self.__total_amount > self.__wealth_limit:
            amount = self.__total_amount * decimal.Decimal(self.__wealth_tax_rate) / 100
            self.__total_amount -= amount
            self.__add_to_log('wealth tax', amount)

    def __add_loyalty_dividends(self):
        if self.__operation_count % self.__loyalty_period == 0:
            amount = self.__total_amount * decimal.Decimal(self.__loyalty_rate) / 100
            self.__total_amount += amount
            self.__add_to_log('loyalty dividends', amount)

    def __add_to_log(self, operation: str, amount: decimal.Decimal):
        self.__log.append({
            'datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'operation': operation,
            'amount': amount
        })

    def __show_log(self):
        print('\n'.join(map(str, self.__log)))

    def run(self):
        print('Добро пожаловать в банкомат!')

        while True:
            self.__operation_count += 1
            self.__collect_wealth_tax()

            action = input('------------------\n'
                           f'На Вашем счёте {round(self.__total_amount, 2)} у.е.\nЧто Вы хотите сделать?\n'
                           '1 - Пополнить. 2 - Снять. 3 - История операций. 0 - Выйти.\n'
                           'Выбор: ')
            match action:
                case '1':
                    self.__deposit()
                case '2':
                    self.__withdraw()
                case '3':
                    self.__show_log()
                case '0':
                    return
                case _:
                    print('Операция не существует')

            self.__add_loyalty_dividends()


if __name__ == '__main__':
    atm = Atm()
    atm.run()
