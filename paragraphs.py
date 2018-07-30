

# импортируем библиотеку регулярных выражений
import re
# импортируем библиотеки для рисования
import matplotlib.pyplot as plt

def get_paragraphs(text):
    '''Данная данкция принимает на вход строку и возвращает список из абзацев
    text - строка входных данных
    paragraphs2 - список абзацев
    '''

    import re
    
    material = re.findall('\n{1}[\–\w\,\.\;\-\s\:\«\»\?\!\(\)\„\\„\“\”\’\–\…\-\—\:\;\(\)\[\]“]+\n{0,1}', text)
    paragraphs = []

    markers = ['<titl>', '<auth>', '<epig>', '<dvot>', '<chpt>', '<part>', '<book>', '<stnz>', '<song>', '<act_>', '<scen>', '<rmrk>', '<chrt>']
    
    for p in material:
        n = p.split('\n')
        if (len(n) > 0) and n[0:5] not in markers:
            paragraphs += n
    return paragraphs

def get_len_paragraphs(paragraphs):

    paragraphs_len = [] # создаём список список длин абзацев в тексте

    for p in paragraphs:
        # если абзац не равен пустой строке
        if len(p) > 3:
            paragraphs_len.append(len(p)) # добавляем длинну этого абзаца к списку длинн абзацев
    
    return paragraphs_len

def draw_parargaps_graph(paragraphs_len, name):
    l = len(paragraphs_len)
    x = range(l)
    
    plt.plot(x, paragraphs_len)
    plt.title('Динамика длины абзаца в романе "' + name +  '"')
    plt.xlabel('Номер абзаца')
    plt.ylabel('Длинна абзаца')
    plt.show()
    plt.savefig(name + '_длина_абзацев' + '.png', format='png', transparent=True)

def draw_parargaps_hist(paragraphs_len, name):
    num_bins = 100
    fig = plt.hist(paragraphs_len, num_bins, facecolor='blue')
    plt.title('Распределение длинн абзацев в романе "' + name +  '"')
    plt.xlabel('Длинна абзаца')
    plt.ylabel('Количество')
    plt.show()
    #plt.savefig(name+ '_гистограмма_абзацев' '.png', format='png', dpi=100)

def get_dialogs(paragraphs, paragraphs_len):
    '''
    функция принимает на вход список параграфов текста и возвращает списки и параметры
    '''
    p_dialogs = [] # создаём список с 
    p_dialog_bolean = [] # создаём список абзацев текста, принадлежащих к диалогу (1) или нет (0).
    p_dialog_len = [] # создаём список длин даилогов
    dialogs_num = 0 # количесво строк с диалогом
    paragraphs_num = len(paragraphs) # общее количество абзацев

    for p in paragraphs:
        # если абзац не равен пустой строке
        if p.startswith('–') or p.startswith('-') or p.startswith('—'):
            p_dialogs.append(p)
            p_dialog_len.append(len(p))
            p_dialog_bolean.append(1)
            dialogs_num += 1.0
        else:
            p_dialogs.append('')
            p_dialog_len.append(0)
            p_dialog_bolean.append(0)

    # вычисляем общуюю диалогичность текста
    dialogic = 1.0 * dialogs_num / paragraphs_num
    # вычисляем абсолютную диалогичность текста
    dialogic_len = 1.0 * sum(p_dialog_len) / sum(paragraphs_len)
    
    print("Общая диалогичность текста: " + str(dialogic))
    print("Абсолютная диалогичность текста: " + str(dialogic_len))
    
    return p_dialogs, p_dialog_bolean, p_dialog_len, p_dialog_len, dialogic, dialogic_len

def draw_dialogim_map(p_dialog_bolean, name):
    l = len(p_dialog_bolean)
    m = []
    for i in p_dialog_bolean:
        m.append(i*100)
    x = range(l)
    fig = plt.plot(x, m)
    plt.xlabel('Распределение диалогов в романе "' + name +  '"')
    plt.show()
    #plt.savefig(name+ '_диалогичность' '.png', format='png', dpi=100)

if __name__ == '__main__':

    direct = 'Тексты/Романы/'
    name = 'Пирамида'
    form = '.txt'

    x = direct + name + form
    f = open(x, 'r')
    f.seek(0)
    text = f.read()
    f.close()

    paragraphs = get_paragraphs(text)

    paragraphs_len = get_len_paragraphs(paragraphs)

    draw_parargaps_graph(paragraphs_len, name)

    #draw_parargaps_hist(paragraphs_len, name)

    p_dialogs, p_dialog_bolean, p_dialog_len, p_dialog_len, dialogic, dialogic_len = get_dialogs(paragraphs, paragraphs_len)

    #draw_dialogim_map(p_dialog_bolean, name)


