words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
a, b, c, d = words


def result(words):
    print(f'{a * words.get('I')}\n{b * words.get('love')}\n\
{c * words.get('Python')}\n{d * words.get('!')}')


result(words)
