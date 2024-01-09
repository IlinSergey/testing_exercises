import datetime
from decimal import Decimal
from typing import TypedDict

from functions.level_3.models import BankCard, Currency, ExpenseCategory


class Arguments(TypedDict):
    amount: Decimal
    currency: Currency
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime
    catecory: ExpenseCategory