import os

import pytest

from functions.level_4.two_students import Student


@pytest.fixture
def students_list_fabric():
    def make_stusents_list(students_data: list[tuple]) -> list[Student]:
        return [Student(first_name=first_name,
                        last_name=last_name,
                        telegram_account=tg) for first_name, last_name, tg in students_data]
    return make_stusents_list


@pytest.fixture
def filepath(request):
    lines, expected_result = request.param
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file:
        file.writelines([f'{line}\n' for line in lines])

    yield path_to_file, expected_result

    os.remove(path_to_file)
