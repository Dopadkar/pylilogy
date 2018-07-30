#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals



import sys
import codecs
import string

# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.

###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.

def get_words_dict(filename):

    f = open(filename, 'r')
    f.seek(0)
    word_list = f.read().split()

    word_dict = {}
    string_for_strip = string.punctuation + ' ' + '«' + '»' + '„' + '“'
    for word in word_list:
        word = word.strip(string_for_strip).lower()
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def print_words(filename):
    word_dict = get_words_dict(filename)

    for k in sorted(word_dict.keys()):
        print('{0:20} {1:5}'.format(k, word_dict[k]))

def print_top(filename):
    word_dict = get_words_dict(filename)

    #for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:100]:
    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        print('{0:20} {0:10}'.format(k, v))

def main():

    #filename = 'Горе от ума.txt'
    #filename = 'Братья Карамазовы.txt'
    filename = 'Братья Карамазовы-new.txt'
    #"print_words(filename)"

    print_top(filename)

    sys.exit(1)

if __name__ == '__main__':
    main()
