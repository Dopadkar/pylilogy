# -*- coding: utf-8 -*-

import re
#import hurst as hr

import matplotlib.pyplot as plt

def get_words1(text):
    # TO_DO - 
    material = text.split(' ')
    words = []
    not_end = '–,,.;-:«»?!()„„“”’–…-—:;()[]“ –'
    for w in material:
        while len(w) > 1 and w[-1] in not_end:
            w = w[:-1]
        while len(w) > 1 and w[0] in not_end:
            w = w[1:]
        if w not in not_end:
            words.append(w)
            
    words = re.findall('\b([.+])\b', text)

    return words

def get_words2(text):
    text = text.lower()
    words = []
    markers = ['', 'titl', 'auth', 'epig', 'dvot', 'chpt', 'part', '<book>', '<stnz>', '<song>', '<act_>', '<scen>', '<rmrk>', '<chrt>']
    material = re.findall(r'\b[\w-]+\b', text)
    for m in material:
        if m not in markers:
            words.append(m)
    return words

def get_signs(text):
    lst = []
    for t in text:
        if t not in lst:
            lst.append(t)
            print(t)
    return lst

def clear_text(text, x,y):
    while x in text:
        text.replace(x,y)
    return text

def draw_grapgh(x):
    l = len(x)
    x_len = range(l)

    a = sum(x) / l
    
    plt.plot(x_len, x)
    plt.plot([0,l], [a,a])
    plt.title('Динамика длины абзаца в романе')
    plt.xlabel('Номер абзаца')
    plt.ylabel('Длинна абзаца')
    plt.show()
    plt.savefig(name + '_длина_абзацев' + '.png', format='png', transparent=True)


if __name__ == '__main__':
    import numpy as np

    markers = ['', 'titl', 'auth', 'epig', 'dvot', 'chpt', 'part', '<book>', '<stnz>', '<song>', '<act_>', '<scen>', '<rmrk>', '<chrt>']

    name = 'Отцы и дети'
    #name = 'Ulysses-marked'

    x = 'texts/Novels/Russian/' + name + '.txt'
    #x = 'Тексты/Novels/' + name + '.txt'
    f = open(x, 'r')
    f.seek(0)
    text = f.read()
    f.close()

    parts = []
    words = get_words2(text)
    print(words[0:1001])
