from unittest.mock import patch

import pytest

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize('promocode_len, expected_result', [
    (5, 5),
    (10, 10),
    (0, 0),
])
def test__generate_promocode__check_len(promocode_len, expected_result):
    promocode = generate_promocode(promocode_len)
    assert len(promocode) == expected_result


def test__generate_promocode__check_default_len():
    promocode = generate_promocode()
    assert len(promocode) == 8


def test__generate_promocode__is_uppercase_with_default_len():
    promocode = generate_promocode()
    assert promocode == promocode.upper()


def test__generate_promocode__is_uppercase():
    promocode = generate_promocode(10)
    assert promocode == promocode.upper()


@pytest.mark.parametrize('return_value, expected_result', [
    ('A', 'AAAAAAAA'),
    ('N', 'NNNNNNNN'),
])
def test__generate_promocode__with_mock_choice(return_value, expected_result):
    with patch('functions.level_4.three_promocodes.random.choice') as random_choice:
        random_choice.return_value = return_value
        promocode = generate_promocode()
        assert promocode == expected_result
        assert len(random_choice.mock_calls) == 8


def test__generate_promocode__with_monkeypatch_mock_choice(monkeypatch):
    def custom_choice(*args, **kwargs):
        return 'A'
    monkeypatch.setattr('functions.level_4.three_promocodes.random.choice', custom_choice)
    promocode = generate_promocode()
    assert promocode == 'AAAAAAAA'
