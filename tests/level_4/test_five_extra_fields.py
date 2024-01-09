from unittest.mock import patch

import pytest

from functions.level_4.five_extra_fields import (
    fetch_app_config_field, fetch_extra_fields_configuration)


@pytest.mark.parametrize('config_file_path', [
    ({'tool:app-config': {'field1': '42', 'field2': 'Some value', 'field3': 'True'}}, 'field1', '42'),
    ({'tool:app-cfg': {'field23': '42', 'field2': 'Some value', 'field3': 'True'},
      'tool:app-config': {'field1': '42', 'field2': 'Some enother value', 'field3': 'True'}}, 'field3', 'True'),
    ({'bad_section': {'field1': '4', 'field2': 'bad_value', 'field3': 'True'}}, 'field1', None),
], indirect=True)
def test__fetch_app_config_field(config_file_path):
    config_file_path, field_name,  expected_result = config_file_path
    assert fetch_app_config_field(config_file_path, field_name) == expected_result


@pytest.mark.parametrize('data_string, expected_result', [
    ('field1: 42\nfield2: "some_value"\nfield3: True', {'field1': 42, 'field2': 'some_value', 'field3': True}),
    (None, {}),
])
def test__fetch_extra_fields_configuration__with_monkeypatch(monkeypatch, data_string, expected_result):
    def fetch_app_config_field_mock(*args, **kwargs):
        return data_string
    monkeypatch.setattr('functions.level_4.five_extra_fields.fetch_app_config_field',
                        fetch_app_config_field_mock)
    assert fetch_extra_fields_configuration('config.ini') == expected_result


@pytest.mark.parametrize('data_string, expected_result', [
    ('field1: 42\nfield2: "some_value"\nfield3: True', {'field1': 42, 'field2': 'some_value', 'field3': True}),
    (None, {}),
])
def test__fetch_extra_fields_configuration__with_unittest_patch(data_string, expected_result):
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as mock_fetch_app_config_field:
        mock_fetch_app_config_field.return_value = data_string
        assert fetch_extra_fields_configuration('config.ini') == expected_result
