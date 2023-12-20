import datetime
from decimal import Decimal
from typing import TypedDict

import pytest

from functions.level_3.models import (BankCard, Currency, Expense,
                                      ExpenseCategory)


@pytest.fixture
def get_card() -> BankCard:
    return BankCard(last_digits='1234', owner='John Doe')


@pytest.fixture
def expenses_list(get_card) -> list[Expense]:
    return [Expense(amount=Decimal('351.30'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 126551),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('473.82'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='alfa-pharm', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 126620),
                    category=ExpenseCategory.MEDICINE_PHARMACY),
            Expense(amount=Decimal('634.83'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='gg platform', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 126668),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('959.98'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='kino park', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 126726),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE),
            Expense(amount=Decimal('87.65'), currency=Currency.USD,
                    card=get_card,
                    spent_in='kino park', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 126782),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE),
            Expense(amount=Decimal('150.00'), currency=Currency.USD,
                    card=get_card,
                    spent_in='apple.com/bill', spent_at=datetime.datetime(2023, 11, 8, 17, 53, 28, 126782),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('150.00'), currency=Currency.USD,
                    card=get_card,
                    spent_in='apple.com/bill', spent_at=datetime.datetime(2023, 10, 8, 17, 53, 28, 126782),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('150.00'), currency=Currency.USD,
                    card=get_card,
                    spent_in='apple.com/bill', spent_at=datetime.datetime(2023, 9, 8, 17, 53, 28, 126782),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('451.87'), currency=Currency.USD,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 126847),
                    category=None),
            Expense(amount=Decimal('637.10'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 126903),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('672.10'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='farm', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127247),
                    category=ExpenseCategory.MEDICINE_PHARMACY),
            Expense(amount=Decimal('465.77'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127300),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('48.25'), currency=Currency.USD,
                    card=get_card,
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127334),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                    category=ExpenseCategory.TRANSPORT),

            Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                    card=get_card,
                    spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                    category=ExpenseCategory.TRANSPORT),

            Expense(amount=Decimal('991.78'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='julis', spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127402),
                    category=ExpenseCategory.BAR_RESTAURANT),
            Expense(amount=Decimal('804.19'), currency=Currency.USD,
                    card=get_card,
                    spent_in='bolt.eu', spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127435),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('751.58'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='alfa-pharm', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127468),
                    category=ExpenseCategory.MEDICINE_PHARMACY),
            Expense(amount=Decimal('492.42'), currency=Currency.USD,
                    card=get_card,
                    spent_in='moscow cinema', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127511),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE),
            Expense(amount=Decimal('81.26'), currency=Currency.USD,
                    card=get_card,
                    spent_in='moscow cinema', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127566),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE),
            Expense(amount=Decimal('398.43'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='green apple', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127621),
                    category=None),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 11, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 11, 8, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 10, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 10, 8, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 10, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS),
            Expense(amount=Decimal('610.54'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='www.taxi.yandex.ru', spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('481.93'), currency=Currency.AMD,
                    card=get_card,
                    spent_in='not in category list', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                    category=None),
            Expense(amount=Decimal('337.05'), currency=Currency.RUB,
                    card=get_card,
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)]


class Arguments(TypedDict):
    amount: Decimal
    currency: Currency
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime
    catecory: ExpenseCategory


@pytest.fixture
def expenses_list_fabric():
    def make_expenses_list(arguments: list[Arguments]) -> list[Expense]:
        result = [Expense(amount=argument['amount'],
                          currency=argument['currency'],
                          card=argument['card'],
                          spent_in=argument['spent_in'],
                          spent_at=argument['spent_at'],
                          category=argument['category']) for argument in arguments]
        return result
    return make_expenses_list
