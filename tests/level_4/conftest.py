import configparser
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


@pytest.fixture
def config_file_path(request):
    data, field_name, expected_result = request.param
    config = configparser.ConfigParser()
    path_to_file = 'config.ini'

    for section, section_data in data.items():
        config.add_section(section)
        for field, value in section_data.items():
            config.set(section, field, value)

    with open(path_to_file, 'w') as config_file:
        config.write(config_file)

    yield path_to_file, field_name, expected_result

    os.remove(path_to_file)
