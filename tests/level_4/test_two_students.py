import pytest

from functions.level_4.two_students import Student, get_student_by_tg_nickname


@pytest.mark.parametrize('tg_username, expected_result', [
    ('squarepants', Student('Bob', 'Sponge', '@squarepants')),
    ('sandy', None),
])
def test__get_student_by_tg_nickname(tg_username, students_list_fabric, expected_result):
    assert get_student_by_tg_nickname(
        telegram_username=tg_username,
        students=students_list_fabric([('Bob', 'Sponge', '@squarepants'),
                                       ('Patrik', 'Star', '@patrikstar'),
                                       ('Tentacles', 'Squidward', '@squiddy'),
                                       ('Cheeks', 'Sandy', None),])
    ) == expected_result


def test__get_student_by_tg_nickname__with_empty_student_list():
    assert get_student_by_tg_nickname(
        telegram_username='squarepants', students=[]) is None
