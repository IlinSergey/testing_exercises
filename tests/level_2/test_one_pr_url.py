import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__succes():
    correct_url = 'https://github.com/user/some_repository/pull/1'
    result = is_github_pull_request_url(correct_url)
    assert result is True


@pytest.mark.parametrize('url, expected_result', [
    ('github.com/user/some_repository/pull/1', False),
    ('https://gitlub.com/user/some_repository/pull/1', False),
    ('https://github.com/user/some_repository/push/1', False),
    ('https://github.com/user/some_repository/push/1/2', False),
])
def test__is_github_pull_request_url__wrong_url(url, expected_result):
    assert is_github_pull_request_url(url) == expected_result


@pytest.mark.parametrize('url', [
    ([
       'https://github.com/user/some_repository/pull/1',
       'https://github.com/user/some_repository/pull/2'
    ]),
    (100_000),
])
def test__is_github_pull_request_url__with_error(url):
    with pytest.raises(AttributeError):
        is_github_pull_request_url(url)
