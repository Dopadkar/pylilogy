x = 'Тексты/Пирамида.txt'
f = open(x, 'r')
f.seek(0)
text = f.read()

# импортируем библиотеку регулярных выражений
import re
# импортируем библиотеки для рисования
import matplotlib.pyplot as plt

paragraphs = re.findall('\n{1}[\–\w\,\.\;\-\s\:\«\»\?\!\(\)\„\“]+\n{0,1}', text)

paragraphs2 = []

for p in paragraphs:
    n = p.split('\n')
    if len(n) > 0:
        paragraphs2 += n

p_len = [] # создаём список список длин абзацев в тексте
p_list = [] # создаём список абзацев текста
p_dialog = [] # создаём список абзацев текста, принадлежащих к диалогу (1) или нет (0).
d = 0 # количесво строк с диалогом
ll = 0 # 

for p in paragraphs2:
    # если абзац не равен пустой строке
    if len(p) > 3:
        p_len.append(len(p)) # добавляем длинну этого абзаца к списку длинн абзацев
        p_list.append(p) # добавляем его в общий список абзацев
        ll += len(p)
        if p.startswith('–'):
            p_dialog.append(1)
            d += 1.0
        else:
            p_dialog.append(0)
    
print(p_len)
print(p_dialog)

l = len(p_len)
x = range(l)

dd = d / l * 100
p_l = ll / l * 100

print("Диалогичность текста: " + str(dd) + "%")
print("Средняя длинна абзаца: " + str(p_l) + "%")

plt.plot(x, p_len)

plt.title('Динамика длинны абзаца в романе')

plt.xlabel('Номер абзаца')
plt.ylabel('Длинна абзаца')

plt.show()
