#def remove_footnotes(text):

import re

filename = 'Евгений Онегин.txt'
a = open(filename, 'r')
a.seek(0)
text = a.read()
a.seek(0)

text = text.replace('&#233;', 'e')
text = text.replace('&#224;', '')
text = text.replace('&#231;', '')
text = text.replace('&#232;', '')
text = text.replace('&#232;', '')
text = text.replace('&#226;', 'ja')
text = text.replace('&#226;', 'ja')

text = text.replace('[', '<')
text = text.replace(']', '>')

# создаём список всех сносок
footnotes = re.findall('<[a-z-A-Za-яА-ЯёЁ()\s0-9.—«»!?,:;\'\*\’&#/…–„“]*>', text)



print(footnotes)

print('Сносок: ' + str(len(footnotes)))

for f in footnotes:
    text = text = text.replace(f, '')
    #if not x: continue

new_filename = filename.replace('.txt', '-new.txt')

b = open(new_filename, 'w')
b.write(text)
a.close()
b.close()
    
