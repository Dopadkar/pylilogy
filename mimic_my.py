#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import sys
import codecs

filename = 'Братья Карамазовы.txt'

def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово 
    со списом слов, которые непосредственно следуют за ним в тексте"""
    
    f = open(filename, 'r')
    f.seek(0)
    word_list = f.read().split()

    res = {}
    prev = ''

    for x in word_list:
        if prev in res:
            res[prev].append(x)
        else:
            res[prev] = [x, ]
        prev = x
    return res


def print_mimic(mimic_dict, word):
    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""
    
    res = []

    for i in xrange(200):
        if not word in mimic_dict:
            word = ''
        word = random.choice(mimic_dict[word])
        res.append(word)

    print(' '.join(res))


def main():
    d = mimic_dict('Братья Карамазовы.txt')
    print_mimic(d, 'Алексей')

if __name__ == '__main__':
    main()
