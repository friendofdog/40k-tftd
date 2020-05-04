import pytest
from tftd import get_strings_from_urls, get_random_str_from_list

def test_get_strings_from_urls():
    strings = get_strings_from_urls([
        'https://wh40k.lexicanum.com/wiki/Thought_for_the_day_(A_-_H)'
    ])
    assert type(strings) is list
    assert all(type(s) is str for s in strings)

def test_get_random_str_from_list():
    list = [
        'Trying to understand weakens the will to act',
        'The Emperor bestows upon us the gift of intolerance',
        'Hope is the beginning of unhappiness',
        'An open mind is like a fortress with its gates unbarred and unguarded'
    ]
    string = get_random_str_from_list(list)
    assert type(string) is str
    assert string in list

