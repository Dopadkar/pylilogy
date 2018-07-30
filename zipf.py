

def get_words_dict(filename):

    import string
    import matplotlib.pyplot as plt
    import sys
    
    f = open(filename, 'r')
    f.seek(0)
    word_list = f.read().split()

    word_dict = {}
    string_for_strip = string.punctuation + ' ' + '«' + '»' + '„' + '“' + '.' + '?'
    for word in word_list:
        word = word.strip(string_for_strip).lower()
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1
            
    nums_list = []
    keys_list = []
    rank_list = []
    r = 0
    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        #print('{0:20} {0:10}'.format(k, v))
        nums_list.append(v)
        keys_list.append(k)
        r += 1
        rank_list.append(r)

    print(nums_list[0:20])
    print(keys_list[0:20])

    plt.title('Распределение частот слов')

    plt.xlabel('Ранг слова')
    plt.ylabel('Частота слова')


    plt.plot(rank_list[0:1000], nums_list[0:1000])
    plt.show()



    sys.exit(1)

if __name__ == '__main__':
    filename = 'Братья Карамазовы-new.txt'
    get_words_dict(filename)
