from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubblesort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day", "I do not think this will turn out well"]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    text = "I think today will be a great day"

    sentiment = extract_sentiment(text)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata3 = [
    ([10, 20, 1, 30, 3, 5], [1, 3, 5, 10, 20, 30]),
    ([25, 7, 3, 4, 6, 8], [3, 4, 6, 7, 8, 25])
]


@pytest.mark.parametrize('sample, expected', testdata3)
def test_bubble_sort(sample, expected):
    assert bubblesort(sample) == expected
