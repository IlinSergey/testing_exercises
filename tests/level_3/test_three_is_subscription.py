import pytest

from functions.level_3.three_is_subscription import is_subscription


@pytest.mark.parametrize('index, expected_result', [
    (5, True),
])
def test__is_subscription__success(index, expected_result, expenses_list):
    assert is_subscription(expenses_list[index], expenses_list) == expected_result


@pytest.mark.parametrize('index, expected_result', [
    (-1, False),
    (0, False),
])
def test__is_subscription__with_not_subscribe(index, expected_result, expenses_list):
    assert is_subscription(expenses_list[index], expenses_list) == expected_result


@pytest.mark.parametrize('index, expected_result', [
    (-4, False),
])
def test__is_subscription__with_many_expenses_by_month(index, expected_result, expenses_list):
    assert is_subscription(expenses_list[index], expenses_list) == expected_result
