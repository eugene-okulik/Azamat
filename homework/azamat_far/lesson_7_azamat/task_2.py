words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
a, b, c, d = words


def result(words):
    for word, count in words.items():
        print(word * count)


result(words)
