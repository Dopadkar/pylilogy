class Book():
    '''
    Это классс, предназначенный для хранения и представления информации отдельных текстов и их частей
    '''
    
    def __init__(self, filename):

        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
        self.punctuation = '–,.-"*:«»#&?!()„“”’–…-—;)—…'
         
        self.paragraphs = []
       
        self.tokens = []
        self.words = []
        
        self.prefrace = []
        self.chapters = []
        self.epilogue = []


        self.str_for_reg_ex = '([–\w\,\.\-\"\№\<\>\'\*\s\:\«\»\#\&\?\!\(\)\„\“\”\’\–\…\-\—\;\(\)\[\]]+)'

        self.from_text(filename)
        self.get_structure()
        self.metadata()
        
    def get_reg_ex(self, marker):
        s = ''.join([marker[0], self.str_for_reg_ex, marker[1]])
        return s
        
    def from_text(self, filename):
        f = open(filename, 'r')
        f.seek(0)
        self.data = f.read()
        f.close()

        #print(self.data[:1000])
        
        #self.data.decode()
        
        self.data = self.data.replace(u'\xa0', u' ')
        self.data = self.data.replace(u'\t', u' ')
        self.data = self.data.replace(u'„', u'«')
        self.data = self.data.replace(u'“', u'»')
        self.data = self.data.replace(u'\n\n', u'\n')
        self.data = self.data.replace(u'\n \n', u'\n')
        self.remove_notes()
        
        self.signs = self.get_signs(self.data)
        
    def get_structure(self, method='patterns'):

        if method == 'reg_ex':
            import re

            self.title = re.findall(self.get_reg_ex(['<titl>', '</titl>']), self.data)
            self.author = re.findall(self.get_reg_ex(['<auth>', '</auth>']), self.data)
            self.code = re.findall(self.get_reg_ex(['<code>', '</code>']), self.data)
            self.year = re.findall(self.get_reg_ex(['<year>', '</year>']), self.data)
            self.prefrace = re.findall(self.get_reg_ex(['<pref>', '</pref>']), self.data)
            self.chapters = re.findall(self.get_reg_ex(['<chpt>', '</chpt>']), self.data)
            self.chapters_names = re.findall(self.get_reg_ex(['<chpn>', '</chpn>']), self.data)
            self.epilogue = re.findall(self.get_reg_ex(['<epil>', '</epil>']), self.data)
        else:
            self.title = self.get_patterns(['<titl>', '</titl>'], self.data)[0]
            self.author = self.get_patterns(['<auth>', '</auth>'], self.data)[0]
            self.code = self.get_patterns(['<code>', '</code>'], self.data)[0]
            self.year = self.get_patterns(['<year>', '</year>'], self.data)[0]
            self.prefrace = self.get_patterns(['<pref>', '</pref>'], self.data)
            self.chapters = self.get_patterns(['<chpt>', '</chpt>'], self.data)
            self.chapters_names = self.get_patterns(['<chpn>', '</chpn>'], self.data)
            self.epilogue = self.get_patterns(['<epil>', '</epil>'], self.data)

        print(type(self.prefrace), len(self.prefrace))
        print(type(self.chapters), len(self.chapters))
        print(type(self.epilogue), len(self.epilogue))

        self.get_text()

    def get_text(self):
        if self.chapters == []:
            self.get_structure()
        self.text = self.prefrace + self.chapters + self.epilogue

    def get_tokens(self):
        if self.text == []:
            self.get_text()
        self.tokens = self.text.split(' ')

    def get_words(self, text='', para='no', lowcase='no'):
        self.words = []
        material = []
        for t in self.tokens:
            if '\n' in t:
                t = t.split('\n')
                for i in t:
                    if i != '':
                        material.append(i)
                    else:
                        material.append('\n' + i)
        self.stuf = []
        
        for t in material:
            if t != '' or t not in self.punctuation:
                if para=='no':
                    if t[0] == '\n':
                        t = t[1:]
                    elif t[-1] == '\n':
                        t = t[:-1]
                if len(t) > 0 and self.isletter(t):
                    if len(t) > 0:
                        while t[0] in self.punctuation:
                            t = t[1:]
                        while t[-1] in self.punctuation:
                            t = t[:-1]
                    if lowcase=='yes':
                        t = t.lower()
                    self.words.append(t)
                else:
                    self.stuf.append(t)
                               
        print('Всего слов: ', len(self.words), ' Уникальных: ', len(set(self.words)))
            
    def isletter(self, token):
        flag = False
        for s in token:
            if s.lower() in self.alphabet:
                flag = True
        return flag

    def metadata(self):
        print("Название: ", self.title)
        print("Автор: ", self.author)
        print("Код: ", self.code)
        print("Год написания: ", self.year)
        
        if self.prefrace == []:
            print('Предисловия нет')
        else:
            print('Предисловие есть')

        if self.epilogue  == []:
            print('Эпилога нет')
        else:
            print('Эпилог есть')
            
        if len(self.chapters) == len(self.chapters_names):
            print('Количество глав:', len(self.chapters))
        else:
            print("Считанных глав: ", len(self.chapters))
            print('Названных глав: ', len(self.chapters_names))

        
        self.text = ' '.join(self.text)
        
        print(len(self.text), ' знаков')
        
    def check(self):

        print(self.data.count('<chpt>'))
        sns = []
        for ch in self.chapters:
            a = self.get_signs(ch)
            sns.append(a)

        s = ''
        for i in self.chapters:
            if i not in s:
                s += i
            
        new_signs = self.get_signs(s)
        print(new_signs)
        print(len(self.signs), len(new_signs))
        missed = []
        for ss in self.signs:
            if ss not in new_signs:
                missed.append(ss)

        print(self.signs)
        print('Пропущены: ', missed)
        
        self.tokens = s.split(' ')
        p = 0
        for t in self.tokens:
            if u'\t' in t:
                p +=1
        print("Табуляций: ", p)
                
    def get_patterns(self, tags, text):
        patterns = []
        a = tags[0]
        b = tags[1]

        s = ''
        tag = a
        end = ''
        for t in text:
            s += t
            len_tag = len(tag)
            if len(s) > len_tag:
                end = s[-len_tag:]
            #print(t, tag, len_tag, end, st)

            if end == a:
                s = ''
                tag = b
                end = ''
            if end == b:
                pattern = s[:-len(b)]
                patterns.append(pattern)
                s = ''
                tag = a
                end = ''
        return patterns

    def remove_notes(self):
        patterns = self.get_patterns(['[', ']'], self.data)
        for p in patterns:
            self.data = self.data.replace('[' + p + ']', '')
        
    def get_signs(self, text):
        signs = []
        for s in text:
            if s not in signs:
                signs.append(s)
        return signs

if __name__ == '__main__':
    print('Ok')
    my_path = "texts/Novels/Russian/"
    filename = "Преступление и наказание.txt"
    book = Book(my_path+filename)
    print(type(book.text))
    text = book.text
    print(type(text))
    book.get_tokens()
    print(len(book.tokens))
    book.get_words()
