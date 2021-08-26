from books import *
from names import *

my_path = "texts/Novels/Russian/"
filename = "Преступление и наказание.txt"

book = Book(my_path+filename)

print(type(book.text))
text = book.text
print(type(text))
book.get_tokens()
book.get_words()

name = Names()
name.get_names(book.words)

for ch in book.chapters:
    if '<chpn>II</chpn>' in ch:
        print(ch[:100])




