import numpy as np

name1 = 'Братья Карамазовы'

x = 'Тексты/Романы/' + name1 + '.txt'
f = open(x, 'r')
f.seek(0)
text1 = f.read()
f.close()


name2 = 'Война и мир'

x = 'Тексты/Романы/' + name2 + '.txt'
f = open(x, 'r')
f.seek(0)
text2 = f.read()
f.close()


# импортируем библиотеку регулярных выражений
import re
# импортируем библиотеки для рисования
import matplotlib.pyplot as plt
import string
import math
import numpy as np

def clear_text(text, x,y):
    for t in text:
        if t == x:
            text.replace(x,y)
    return text

def draw_frequence(freq_list, name= ''):
    l = len(freq_list)
    x = range(l)
    plt.plot(x, freq_list)
    plt.title('Функция плотности распреления букв в романе "' + name +  '"')
    plt.xlabel('Буквы')
    plt.ylabel('Частота встречаемости')
    plt.show()
    plt.savefig(name + '_распреления букв' + '.png', format='png', transparent=True)

def get_difference(freq1, freq2, dist='Normal'):
    f1 = np.array(freq1)
    f2 = np.array(freq2)
    if dist=='Normal':
        diff = np.subtract(f1,f2)
        d = diff.tolist()
        df = []
        for i in d:
            df.append(abs(i))
        df = sum(df)
        return df
    elif dist=='Euclide':
        return np.linalg.norm(f1 - f2)

def get_frequence(text, alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя', name=''):
    freq_abs = [0] * len(alphabet)
    freq_rat = []

    text = text.lower()

    for x in text:
        if x in alphabet:
            freq_abs[alphabet.index(x)] += 1

    total = sum(freq_abs)
    for x in freq_abs:
        freq_rat.append(1.0 * x / total)
        
    return freq_abs, freq_rat
    draw_frequence(freq_list, name)

alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'

text1 = clear_text(text1, 'ё','е')
text2 = clear_text(text2, 'ё','е')

freq_abs1, freq_rat1 = get_frequence(text1, alphabet)
freq_abs1, freq_rat2 = get_frequence(text2, alphabet)

d1 = get_difference(freq_rat1, freq_rat2)

print('Normal мкжду ', name1, ' и ', name2 ': ',d1)

d2 = get_difference(freq_rat1, freq_rat2, 'Euclide')

print('Euclide мкжду ', name1, ' и ', name2 ': ',, d2)
