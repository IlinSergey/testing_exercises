import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize('text, expected_result', [
    ('Этот текст не несет в себе никаких эмоций.', None),
    ('Погода сегодня так себе, не слишком хорошо, но и не плохо. Все как обычно.', None),
    ('Сегодня просто восхитительно! На улице прекрасно, удивительно солнечно и интересно.', 'GOOD'),
    ('У меня проблемы, кругом один негатив, это печально и грустно.', 'BAD'),
    ('Some_long_long_long_long_text', None),
])
def test__check_tweet_sentimemt__succes(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text=text, good_words=good_words,
                                 bad_words=bad_words) == expected_result


@pytest.mark.parametrize('text, good_words, bad_words, expected_error', [
    (123, {'good', 'word'}, {'bad', 'word'}, AttributeError),
    ('Some text', 123, {'bad', 'evil'}, TypeError),
])
def test__check_tweet_sentiment__with_error(text, good_words, bad_words, expected_error):
    with pytest.raises(expected_error):
        check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)
