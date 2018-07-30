import re
name = "school-base.txt"
handle = open(name)
emails = list()
for line in handle:
    if re.search('^Адрес сайта: ', line):
        #print(line)
        s = re.findall(r'[\d\w\S-]+@[\d\w\S\.-]+', line)
        print(s)
        #emails.append(s)

#print(emails)
