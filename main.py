# Case-study #3
# Developers: Maltsev A., Kolchik K.
#
import ru_local as ru

MAX_MONTH = 12
TAX_RATES = ['', 0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
ONE_SUBJECT_LOWER_LIMITS = ['', 0, 9076, 36901, 89351, 186351, 405101, 406751]
MARRIED_COUPLE_LOWER_LIMITS = ['', 0, 18151, 73801, 148851, 226851, 405101, 457601]
ONE_PARENT_LOWER_LIMITS = ['', 0, 12951, 49401, 127551, 206601, 405101, 432201]


def year_income():
    '''
    The function calculates the annual income.
    '''

    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.YEAR_INCOME} {ru.NAME[month]} [USD]: '))
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


def sum_series_one_subject(n, D):
    '''
    Function that calculates tax on an interval.
    '''
    res = 0
    for i in range(1, n):
        value = TAX_RATES[i] * (D - ONE_SUBJECT_LOWER_LIMITS[i])
        res += value
    return res


def sum_series_married_couple(n, D):
    '''
    Function that calculates tax on an interval.
    '''
    res = 0
    for i in range(1, n):
        value = TAX_RATES[i] * (D - MARRIED_COUPLE_LOWER_LIMITS[i])
        res += value
    return res


def sum_series_one_parent(n, D):
    '''
    Function that calculates tax on an interval.
    '''
    res = 0
    for i in range(1, n):
        value = TAX_RATES[i] * (D - ONE_PARENT_LOWER_LIMITS[i])
        res += value
    return res


def one_subject_tax(D):
    '''
    Function that calculates tax for one subject.
    '''
    amount = 0
    if 0 < D <= 9075:
        amount = sum_series_one_subject(1, D)
    elif 9076 <= D <= 36900:
        amount = sum_series_one_subject(2, D)
    elif 36901 <= D <= 89350:
        amount = sum_series_one_subject(3, D)
    elif 89351 <= D <= 186350:
        amount = sum_series_one_subject(4, D)
    elif 186351 <= D <= 405100:
        amount = sum_series_one_subject(5, D)
    elif 405101 <= D <= 406750:
        amount = sum_series_one_subject(6, D)
    else:
        amount = sum_series_one_subject(7, D)

    return amount


def married_couple_tax(D):
    '''
    Function that calculates tax for couple.
    '''
    amount = 0
    if 0 < D <= 18150:
        amount = sum_series_married_couple(1, D)
    elif 18151 <= D <= 73800:
        amount = sum_series_married_couple(2, D)
    elif 73801 <= D <= 148850:
        amount = sum_series_married_couple(3, D)
    elif 148851 <= D <= 226850:
        amount = sum_series_married_couple(4, D)
    elif 226851 <= D <= 405100:
        amount = sum_series_married_couple(5, D)
    elif 405101 <= D <= 457600:
        amount = sum_series_married_couple(6, D)
    else:
        amount = sum_series_married_couple(7, D)

    return amount


def one_parent_tax(D):
    '''
    Function that calculates tax for one parent.
    '''
    amount = 0
    if 0 < D <= 12950:
        amount = sum_series_one_subject(1, D)
    elif 12951 <= D <= 49400:
        amount = sum_series_one_subject(2, D)
    elif 49401 <= D <= 127550:
        amount = sum_series_one_subject(3, D)
    elif 127551 <= D <= 206600:
        amount = sum_series_one_subject(4, D)
    elif 206601 <= D <= 405100:
        amount = sum_series_one_subject(5, D)
    elif 405101 <= D <= 432201:
        amount = sum_series_one_subject(6, D)
    else:
        amount = sum_series_one_subject(7, D)

    return amount


if __name__ == '__main__':
    print(f'{ru.CATEGORY}')
    print(f'{ru.SUBJECT}')
    print(f'{ru.COUPLE}')
    print(f'{ru.PARENT}')
    category = int(input(f'{ru.ENTER} \n'))
    all_year_income = year_income()
    print(f'{ru.ALL_YEAR_INCOME} {all_year_income:.0f}')
    print(f'{ru.ENTER_FREE_INCOME}')
    free_income = free_tax()
    print(f'{ru.FREE_INCOME} {free_income:.0f}')
    print(f'{ru.NOT_FREE_INCOME} {all_year_income - free_income:.0f}')
    year_tax = 0
    if category == 1:
        year_tax = one_subject_tax(all_year_income)
    elif category == 2:
        year_tax = married_couple_tax(all_year_income)
    else:
        year_tax = one_parent_tax(all_year_income)
    print(f'{ru.YEAR_TAX} {year_tax:.0f}')
    print(f'{ru.MONTH_TAX} {year_tax / 12:.0f}')
