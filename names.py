class Names():

    def __init__(self):
        self.names = []

    def get_names(self, words):
        self.low_words = []
        self.lst = []
        self.up_words = []
        words = set(words)

        for w in words:
            if w.islower():
                self.low_words.append(w)
            else:
                self.lst.append(w)

        for w in self.lst:
            if w.lower() not in self.low_words:
                self.up_words.append(w)
                
        print(self.up_words)
