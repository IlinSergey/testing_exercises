import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize('title, max_title_lenght, expected_result', [
    ('Some title', 100, 'Copy of Some title'),
    ('Copy of Some title', 100, 'Copy of Some title (2)'),
    ('Copy of Some title (5)', 10, 'Copy of Some title (5)'),
])
def test_change_copy_item(title, max_title_lenght, expected_result):
    assert change_copy_item(title=title,
                            max_main_item_title_length=max_title_lenght
                            ) == expected_result


big_title = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
             "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
             "when an unknown printer took a galley of type and scrambled it to make a type " \
             "specimen book. It has survived not only five centuries, but also the leap into " \
             "electronic typesetting, remaining essentially unchanged. It was popularised in " \
             "the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, " \
             "and more recently with desktop publishing software like Aldus PageMaker including " \
             "versions of Lorem Ipsum."


@pytest.mark.parametrize('title, expected_result', [
    ('Some title', 'Copy of Some title'),
    ('Copy of Some title', 'Copy of Some title (2)'),
    (big_title, big_title),
])
def test__change_copy_item__with_default_max_lenght(title, expected_result):
    assert change_copy_item(title=title) == expected_result
