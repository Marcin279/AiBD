from textblob import TextBlob
from typing import List
import copy

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)
    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(data: List[int]) -> List[int]:
    data = copy.copy(data)
    changed = True
    j = len(data)
    while changed:
        changed = False
        for i in range(j-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                changed = True
        j -= 1
    return data

