import datetime
from decimal import Decimal

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, \
                                               Expense, parse_ineco_expense

cards = [
    BankCard(last_digits="1234", owner="John Doe"),
    BankCard(last_digits="5678", owner="Jane Smith"),
]

sms = [
    SmsMessage(text='2500.00 RUB, 112223331234 18.11.23 13:31 Magnit authcode 5522',
               author='Bank', sent_at=datetime.datetime.now()),
    SmsMessage(text='1200.50 RUB, 445566775678 19.01.24 15:45 Walmart authcode 1234',
               author='Bank', sent_at=datetime.datetime.now()),
    SmsMessage(text='150.50 RUB, 445566775676 15.01.24 12:45 Ozon authcode 1254',
               author='Bank', sent_at=datetime.datetime.now()),
    SmsMessage(text='0 RUB, 445566775678 19.01.24 15:45 Wildberries authcode 1234',
               author='Bank', sent_at=datetime.datetime.now()),
]

result = [
    Expense(amount=Decimal('2500.00'),
            card=BankCard(last_digits='1234', owner='John Doe'),
            spent_in='Magnit',
            spent_at=datetime.datetime(2023, 11, 18, 13, 31)),
    Expense(amount=Decimal('1200.50'),
            card=BankCard(last_digits='5678', owner='Jane Smith'),
            spent_in='Walmart',
            spent_at=datetime.datetime(2024, 1, 19, 15, 45)),
    Expense(amount=Decimal('0'),
            card=BankCard(last_digits='5678', owner='Jane Smith'),
            spent_in='Wildberries',
            spent_at=datetime.datetime(2024, 1, 19, 15, 45)),
]


@pytest.mark.parametrize('sms, cards, expected_result', [
    (sms[0], cards, result[0]),
    (sms[1], cards, result[1]),
    (sms[3], cards, result[2]),
])
def test_parse_ineco_expense(sms, cards, expected_result):
    assert parse_ineco_expense(sms=sms, cards=cards) == expected_result


@pytest.mark.parametrize('sms, cards', [(sms[2], cards),])
def test_parse_ineco_expense_with_error(sms, cards):
    with pytest.raises(IndexError):
        parse_ineco_expense(sms=sms, cards=cards)
