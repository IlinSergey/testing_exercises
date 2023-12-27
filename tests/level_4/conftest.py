
import pytest

from functions.level_4.two_students import Student


@pytest.fixture
def students_list_fabric():
    def make_stusents_list(students_data: list[tuple]) -> list[Student]:
        return [Student(first_name=first_name,
                        last_name=last_name,
                        telegram_account=tg) for first_name, last_name, tg in students_data]
    return make_stusents_list
