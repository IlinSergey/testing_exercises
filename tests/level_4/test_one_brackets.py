import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize('name, expected_result', [
    ('{Hello World!}', 'ello World'),
    ('{Hello World!', 'ello Worl'),
    ('Hello World!', 'Hello World!'),
    ('{{Hello World!}}', 'Hello World!'),
    (' ', ' '),
])
def test__delete_remove_brackets_quotes(name, expected_result):
    assert delete_remove_brackets_quotes(name) == expected_result
