import pytest
from tftd import get_strings_from_urls

def test_get_strings_from_urls():
    strings = get_strings_from_urls([
        'https://wh40k.lexicanum.com/wiki/Thought_for_the_day_(A_-_H)'
    ])
    assert type(strings) is list
    assert all(type(s) is str for s in strings)
