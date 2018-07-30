import re

def download_markers(filename):
    
    direct = 'Sources/'
    form = '.txt'

    x = direct + filename + form
    f = open(x, 'r')
    f.seek(0)
    m = f.read()
    f.close()

    m = m.split(',')

    markers = []

    for mark in m:
        markers.append(mark[0:6])

    print(markers)

    return markers

def count_marker(marker, text):
    '''
    Функция принимает на вход строку с названием маркера marker и строку с текстом text и аозвращает число упоминаний маркера в тексте.

    '''
    return text.count(marker)

def count_markers(markers, text):
    '''
    Функция принимает на вход список строк с названиями маркеров markers и строку с текстом  и аозвращает список с числами упоминаний маркера в тексте.

    '''
    markers_count = []
    for marker in markers:
        markers_count.append(count_marker(marker, text))
    
    return markers_count

def delete_marker(marker, text):
    '''
    
    '''
    return text.replace(marker,'')

def delete_markers():

    for marker in markers:
        text = text.replace(marker,'')
    
    return text

if __name__ == '__main__':
    download_markers('markers')
