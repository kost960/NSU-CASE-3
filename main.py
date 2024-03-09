import ru_local as ru

MAX_MONTH = 12
TAX_RATES = ['', 0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
ONE_SUBJECT_LOWER_LIMITS = ['', 0, 9076, 36901, 89351, 186351, 405101, 406751]

def year_income():
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'Доход в {ru.NAME[month]} [USD]: '))
        amount += value
    return amount

def free_tax():
    '''
    The function determines the annual tax-free amount.
    '''
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TEXT_FREE_TAX} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount

def sum_series(n, D):
    res = 0
    for i in range(1, n):
        value = TAX_RATES[i]*(D - ONE_SUBJECT_LOWER_LIMITS[i])
        res += value
    return res


def one_subject_tax(D):
    amount = 0
    if 0 < D <= 9075:
        amount = sum_series(1, D)
    elif 9076 <= D <= 36900:
        amount = sum_series(2, D)
    elif 36901 <= D <= 89350:
        amount = sum_series(3, D)
    elif 89351 <= D <= 186350:
        amount = sum_series(4, D)
    elif 186351 <= D <= 405100:
        amount = sum_series(5, D)
    elif 405101 <= D <= 406750:
        amount = sum_series(6, D)
    else:
        amount = sum_series(7, D)

    return amount

if __name__ == '__main__':
    print('Укажите категорию налогоплательщика: ')
    print('1. Субъект')
    print('2. Супружеская пара')
    print('3. Один родитель')
    category = int(input('Введите значение [1-3]: '))
    all_year_income = year_income()
    print(all_year_income)
    free_income = free_tax()
    print(free_income)
    print(all_year_income - free_income)
    year_tax = 0
    if category == 1:
        year_tax = one_subject_tax(all_year_income)
    print(year_tax)
    print(year_tax/12)