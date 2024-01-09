import datetime
from decimal import Decimal

import pytest
from custom_types import Arguments

from functions.level_3.models import BankCard, Currency, ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


@pytest.mark.parametrize('arguments, expected_result', [
    ([Arguments(amount=Decimal('351.30'),
                currency=Currency.RUB,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='chinar',
                spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 126551),
                category=ExpenseCategory.SUPERMARKET)],
     ExpenseCategory.SUPERMARKET),
    ([Arguments(amount=Decimal('473.82'),
                currency=Currency.EUR,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='alfa-pharm',
                spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 126620),
                category=ExpenseCategory.MEDICINE_PHARMACY)],
     ExpenseCategory.MEDICINE_PHARMACY),
    ([Arguments(amount=Decimal('337.05'),
                currency=Currency.RUB,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='zoom.us',
                spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)],
     ExpenseCategory.ONLINE_SUBSCRIPTIONS),
    ([Arguments(amount=Decimal('481.93'),
                currency=Currency.AMD,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='not in category list',
                spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                category=None)],
     None),
])
def test__guess_expense_category__succes(arguments, expenses_list_fabric, expected_result):
    assert guess_expense_category(expenses_list_fabric(arguments)[0]) == expected_result
