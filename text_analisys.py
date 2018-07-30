#x = input('Название файла: ')

direct = 'Тексты/Романы/'
name = 'Мастер и Маргарита'
form = '.txt'

x = direct + name + form
f = open(x, 'r')
f.seek(0)
text = f.read()
f.close()

name2 = 'Война и мир'
form = '.txt'

x = direct + name2 + form
f = open(x, 'r')
f.seek(0)
text2 = f.read()
f.close()








import statistics as stt
import paragraphs as ph
import nltk
import leters as lt


paragraphs = ph.get_paragraphs(text)

paragraphs_len = ph.get_len_paragraphs(paragraphs)
'''
p_len_mean = stt.mean(paragraphs_len)
p_len_mode = stt.mode(paragraphs_len)
p_len_median = stt.median(paragraphs_len)
'''
print('Название файла: ' + name)

text_len_s = len(text)
print('Длинна в знаках: ' + str(text_len_s))

punctuation = 1.0 * (text.count('.') + text.count(',') + text.count('?') + text.count(';') + text.count('.') + text.count('!') + text.count('-')) / len(text)

alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'

text = lt.clear_text(text, 'ё','е')
text2 = lt.clear_text(text2, 'ё','е')

freq_abs1, freq_rat1 = lt.get_frequence(text, alphabet)
freq_abs2, freq_rat2 = lt.get_frequence(text2, alphabet)

d1 = lt.get_difference(freq_rat1, freq_rat2)

print('Normal мкжду ', name,'-', name2, d1)

d2 = lt.get_difference(freq_rat1, freq_rat2, 'Euclide')

print('Euclide мкжду ', d2)

lt.draw_frequence(freq_rat1, name=name)



# работа со словами



text2 = text.split(' ')

#text2 = nltk.word_tokenize(text)

m = len(text2)

'''
#text2.dispersion_plot(["Алексей", "Иван", "Смердяков", "Дмитрий"])
fdist = nltk.FreqDist(text2)
print(fdist)
vocabulary1 = fdist.keys()
vocabulary1[:50]
'''

print('Длинна в словах: ' + str(m))

#print('Средняя длина абзаца: ' + str(p_len_mean))
#print('Мода длина абзаца: ' + str(p_len_mode))
#print('Медиана длина абзацах: ' + str(p_len_median))


n = len(set(text2))
print('Длинна в уникалных словах: ' + str(n))
u = n/m
print('Уникальность: ' + str(u))

print('Пунктуационная плотность: ' + str(punctuation))

p_dialogs, p_dialog_bolean, p_dialog_len, p_dialog_len, dialogic, dialogic_len = ph.get_dialogs(paragraphs, paragraphs_len)

ph.draw_parargaps_graph(paragraphs_len, name)

ph.draw_parargaps_hist(paragraphs_len, name)

#ph.draw_dialogim_map(p_dialog_bolean, name)




