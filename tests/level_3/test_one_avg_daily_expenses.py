import datetime
from decimal import Decimal

from conftest import Arguments

from functions.level_3.models import Currency, ExpenseCategory
from functions.level_3.one_avg_daily_expenses import \
    calculate_average_daily_expenses


def test__calculate_average_daily_expenses__succes(expenses_list):
    assert calculate_average_daily_expenses(expenses_list) == Decimal('1639.58')


def test__calculate_average_daily_expenses__with_zero_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([Arguments(amount=Decimal('0.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='leetcode.com',
                                           spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                                           category=ExpenseCategory.TRANSPORT),
                                 Arguments(amount=Decimal('0.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='leetcode.com',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                           category=ExpenseCategory.SUPERMARKET),
                                 Arguments(amount=Decimal('0.00'),
                                           currency=Currency.RUB,
                                           card=card,
                                           spent_in='leetcode.com',
                                           spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                           category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)])
    assert calculate_average_daily_expenses(data) == Decimal('0.00')


def test__calculate_average_daily_expenses__with_equal_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([Arguments(amount=Decimal('150.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='doc',
                                           spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                                           category=ExpenseCategory.TRANSPORT),
                                 Arguments(amount=Decimal('150.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='chinar',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                           category=ExpenseCategory.SUPERMARKET),
                                 Arguments(amount=Decimal('150.00'),
                                           currency=Currency.RUB,
                                           card=card,
                                           spent_in='zoom.us',
                                           spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                           category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)])
    assert calculate_average_daily_expenses(data) == Decimal('150.00')


def test__calculate_average_daily_expenses__with_equal_dates(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([Arguments(amount=Decimal('100.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='doc',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                                           category=ExpenseCategory.TRANSPORT),
                                 Arguments(amount=Decimal('50.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='chinar',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                           category=ExpenseCategory.SUPERMARKET),
                                 Arguments(amount=Decimal('150.00'),
                                           currency=Currency.RUB,
                                           card=card,
                                           spent_in='zoom.us',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127785),
                                           category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)])
    assert calculate_average_daily_expenses(data) == Decimal('300.00')


def test__calculate_average_daily_expenses__with_negative_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([Arguments(amount=Decimal('-100.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='doc',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                                           category=ExpenseCategory.TRANSPORT),
                                 Arguments(amount=Decimal('-100.00'),
                                           currency=Currency.AMD,
                                           card=card,
                                           spent_in='chinar',
                                           spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                           category=ExpenseCategory.SUPERMARKET),
                                 Arguments(amount=Decimal('-150.00'),
                                           currency=Currency.RUB,
                                           card=card,
                                           spent_in='zoom.us',
                                           spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                           category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)])
    assert calculate_average_daily_expenses(data) == Decimal('-175.00')
