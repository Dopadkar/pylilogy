#x = input('Название файла: ')

direct = 'Тексты/'
name = 'Мертвые души'
form = '.txt'

x = direct + name + form
f = open(x, 'r')
f.seek(0)
text = f.read()
f.close()

import paragraphs as ph

paragraphs = ph.get_paragraphs(text)

paragraphs_len = ph.get_len_paragraphs(paragraphs)

ph.draw_parargaps_graph(paragraphs_len, name)

ph.draw_parargaps_hist(paragraphs_len, name)

p_dialogs, p_dialog_bolean, p_dialog_len, p_dialog_len, dialogic, dialogic_len = ph.get_dialogs(paragraphs, paragraphs_len)

#ph.draw_dialogim_map(p_dialog_bolean, name)

print('Название файла: ' + name)





print('Длинна в знаках: ' + str(c))
text2 = text.split(' ')
m = len(text2)
print('Длинна в словах: ' + str(m))


n = len(set(text2))
print('Длинна в уникалных словах: ' + str(n))
u = n/m
print('Уникальность: ' + str(u))
