import requests
from bs4 import BeautifulSoup
from collections import Counter


def func1(url, clamp):
    return format_text(func2(url), clamp)


def func2(url):
    return my_dict(my_start(url))


def my_start(url):
    wordlist = []
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    text = soup.text
    words = text.lower().split()
    for word in words:
        wordlist.append(word)

    cleanlist = []
    symbols = '!@#$%^&*▲→↵()_—−-+=»{[}]|\;:"<>?/., '
    for word in wordlist:
        for char in range(0, len(symbols)):
            word = word.replace(symbols[char], '')
        if len(word) > 0:
            cleanlist.append(word)
    return cleanlist


def my_dict(cleanlist):
    word_count = {}
    for word in cleanlist:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def format_text(words, clamp):
    counter = Counter(words)
    text = ""
    if clamp > 0:
        for key, value in counter.most_common(clamp):
            text += key + " => " + str(value) + "\n"
    else:
        for key, value in counter.most_common():
            text += key + " => " + str(value) + "\n"
    return text