import pytest

from functions.level_4.four_lines_counter import count_lines_in


@pytest.mark.parametrize('filepath', [
    (['1', '2', '3',], 3),
    (['#1', '#2', '3'], 1),
    (['#1', '#2', '#3'], 0),
    ([], 0),
    (['', '', ''], 3)
], indirect=True)
def test__count_lines_in(filepath):
    filepath, expected_result = filepath
    assert count_lines_in(filepath) == expected_result


def test__count_lines_in__witn_no_file():
    assert count_lines_in('no_file.txt') is None
