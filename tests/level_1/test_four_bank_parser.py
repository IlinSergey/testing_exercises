import pytest

from functions.level_1.four_bank_parser import parse_ineco_expense


@pytest.mark.parametrize('sms_index, expected_result_index', [
    (0, 0),
    (1, 1),
    (3, 2),
])
def test__parse_ineco_expense(sms_index, expected_result_index,
                              bank_card_list, sms_list, get_result_expenses):
    assert parse_ineco_expense(sms_list[sms_index],
                               bank_card_list) == get_result_expenses[expected_result_index]


@pytest.mark.parametrize('sms_index', [
    2,
])
def test__parse_ineco_expense__with_error(sms_index, sms_list, bank_card_list):
    with pytest.raises(IndexError):
        parse_ineco_expense(sms_list[sms_index], bank_card_list)
