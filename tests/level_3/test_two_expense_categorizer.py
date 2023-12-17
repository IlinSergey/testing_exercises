import datetime
from decimal import Decimal

import pytest

from functions.level_3.models import BankCard, Currency, ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


@pytest.mark.parametrize('arguments, expected_result', [
    ([(Decimal('351.30'), Currency.RUB, BankCard(last_digits='1234', owner='John Doe'),
       'chinar', datetime.datetime(2023, 12, 9, 17, 53, 28, 126551), ExpenseCategory.SUPERMARKET)],
     ExpenseCategory.SUPERMARKET),
    ([(Decimal('473.82'), Currency.EUR, BankCard(last_digits='1234', owner='John Doe'),
       'alfa-pharm', datetime.datetime(2023, 12, 7, 17, 53, 28, 126620), ExpenseCategory.MEDICINE_PHARMACY),],
     ExpenseCategory.MEDICINE_PHARMACY),
    ([(Decimal('337.05'), Currency.RUB, BankCard(last_digits='1234', owner='John Doe'),
       'zoom.us', datetime.datetime(2023, 12, 7, 17, 53, 28, 127785), ExpenseCategory.ONLINE_SUBSCRIPTIONS),],
     ExpenseCategory.ONLINE_SUBSCRIPTIONS),
    ([(Decimal('481.93'), Currency.AMD, BankCard(last_digits='1234', owner='John Doe'),
       'not in category list', datetime.datetime(2023, 12, 8, 17, 53, 28, 127730), None),],
     None),
])
def test__guess_expense_category__succes(arguments, expenses_list_fabric, expected_result):
    assert guess_expense_category(expenses_list_fabric(arguments)[0]) == expected_result
