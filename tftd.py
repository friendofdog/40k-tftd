import requests
from bs4 import BeautifulSoup
from random import randrange

def get_strings_from_urls(urls):
    strings = []
    ignore = [
        'Thought for the day',
        'Letter',
        'Source'
    ]
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('td', align='center')
        for r in results:
            cell = r.find('b')
            if cell is not None:
                text = cell.get_text()
                if len(text) > 2 and not any(i in text for i in ignore):
                    strings.append(text)
    return strings

def get_random_str_from_list(list):
    max = len(list) - 1
    i = randrange(0, max)
    return list[i]

if __name__ == '__main__':
    strings = get_strings_from_urls([
        'https://wh40k.lexicanum.com/wiki/Thought_for_the_day_(A_-_H)',
        'https://wh40k.lexicanum.com/wiki/Thought_for_the_day_(I_-_P)',
        'https://wh40k.lexicanum.com/wiki/Thought_for_the_day_(Q_-_Z)'
    ])

    random_string = get_random_str_from_list(strings)

    print(random_string)
