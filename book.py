import statistics as stt
import paragraphs as ph
import nltk
import leters as lt
import os

class Book():

    def __init__(self, direct, name):
        self.name = name
        self.direct = direct

        x = direct + name 
        f = open(x, 'r')
        f.seek(0)
        self.text = f.read()
        f.close()

    '''
    Методы, работающие со словами
    '''

    def get_words(self):
        self.words = self.text.split(' ')
        string_for_strip = string.punctuation + ' ' + '«' + '»' + '„' + '“'
        self.words_list = []
        for word in word_list:
            word = word.strip(string_for_strip).lower()
            self.words_list.appenr(word)
        return words_list

    def get_len_words(self):
        return len(get_words())

    def get_words_dict(self):
        words = get_words()

        word_dict = {}
        string_for_strip = string.punctuation + ' ' + '«' + '»' + '„' + '“'
        for word in words:
            word = word.strip(string_for_strip).lower()
            if word:
                word_dict[word] = word_dict.get(word, 0) + 1

        return word_dict
    

    '''
    Методы, работающие с буквами
    '''

    def get_leters_frequence():
        alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
        self.text1 = lt.clear_text(self.text, 'ё','е')
        freq_abs1, freq_rat1 = lt.get_frequence(self.text1, alphabet)
        return freq_rat1

    def compare_leters(self, other,):
        alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'

        self.text1 = lt.clear_text(self.text, 'ё','е')
        self.text2 = lt.clear_text(other.text, 'ё','е')

        freq_abs1, freq_rat1 = lt.get_frequence(self.text1, alphabet)
        freq_abs2, freq_rat2 = lt.get_frequence(self.text2, alphabet)

        d1 = lt.get_difference(freq_rat1, freq_rat2)
        return d1

    '''
    Методы, работающие с параграфами
    '''

    def get_paragraphs(self, text):
        paragraphs = ph.get_paragraphs(text)
        paragraphs_len = ph.get_len_paragraphs(paragraphs)

    def get_dialogs(self, text):
        p_dialogs, p_dialog_bolean, p_dialog_len, p_dialog_len, dialogic, dialogic_len = ph.get_dialogs(paragraphs, paragraphs_len)


direct = '/'

name0 = 'Герой нашего времени.txt'

book1 = Book(direct,name0)


d = book1.compare_leters(book2)

print(d)
