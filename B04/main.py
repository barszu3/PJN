import re


def checkIsNone(pattern, input):
    m = re.search(pattern, input)
    x = None
    if m is not None:
        x = m.group()
    return x
f = 'file.txt'
file= open(f, "r", encoding='UTF8')
pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*)'
emails = []
for line in file:
    words = line.split()
    for word in words:
        x = checkIsNone(pattern, word)
        if x is not None:
            emails.append(x)
print(emails)
