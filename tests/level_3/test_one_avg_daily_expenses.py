import datetime
from decimal import Decimal

from functions.level_3.models import Currency, ExpenseCategory
from functions.level_3.one_avg_daily_expenses import \
    calculate_average_daily_expenses


def test__calculate_average_daily_expenses__succes(expenses_list):
    assert calculate_average_daily_expenses(expenses_list) == Decimal('1639.58')


def test__calculate_average_daily_expenses__with_zero_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([(Decimal('0.00'), Currency.AMD,
                                  card, 'doc', datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                                  ExpenseCategory.TRANSPORT),
                                 (Decimal('0.00'), Currency.AMD,
                                  card, 'chinar', datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                  ExpenseCategory.SUPERMARKET),
                                 (Decimal('0.00'), Currency.RUB,
                                  card, 'zoom.us', datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                  ExpenseCategory.ONLINE_SUBSCRIPTIONS),
                                 ])
    assert calculate_average_daily_expenses(data) == Decimal('0.00')


def test__calculate_average_daily_expenses__with_equal_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([(Decimal('150.00'), Currency.AMD,
                                  card, 'doc', datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                                  ExpenseCategory.TRANSPORT),
                                 (Decimal('150.00'), Currency.AMD,
                                  card, 'chinar', datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                  ExpenseCategory.SUPERMARKET),
                                 (Decimal('150.00'), Currency.RUB,
                                  card, 'zoom.us', datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                  ExpenseCategory.ONLINE_SUBSCRIPTIONS),
                                 ])
    assert calculate_average_daily_expenses(data) == Decimal('150.00')


def test__calculate_average_daily_expenses__with_equal_dates(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([(Decimal('100.00'), Currency.AMD,
                                  card, 'doc', datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                                  ExpenseCategory.TRANSPORT),
                                 (Decimal('50.00'), Currency.AMD,
                                  card, 'chinar', datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                  ExpenseCategory.SUPERMARKET),
                                 (Decimal('150.00'), Currency.RUB,
                                  card, 'zoom.us', datetime.datetime(2023, 12, 8, 17, 53, 28, 127785),
                                  ExpenseCategory.ONLINE_SUBSCRIPTIONS),
                                 ])
    assert calculate_average_daily_expenses(data) == Decimal('300.00')


def test__calculate_average_daily_expenses__with_negative_amounts(expenses_list_fabric, get_card):
    card = get_card
    data = expenses_list_fabric([(Decimal('-100.00'), Currency.AMD,
                                  card, 'doc', datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                                  ExpenseCategory.TRANSPORT),
                                 (Decimal('-100.00'), Currency.AMD,
                                  card, 'chinar', datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                                  ExpenseCategory.SUPERMARKET),
                                 (Decimal('-150.00'), Currency.RUB,
                                  card, 'zoom.us', datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                                  ExpenseCategory.ONLINE_SUBSCRIPTIONS),
                                 ])
    assert calculate_average_daily_expenses(data) == Decimal('-175.00')
