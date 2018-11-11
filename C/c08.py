int = [',', '.', '?', '!', ';', ':', '-', '"']
def delete(line):
    for i in int:
        line = line.replace(i,'')
    return line
f = 'file.txt'
file= open(f, "r", encoding='UTF8')
pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*)'
emails = []
words = []
for line in file:
    line = delete(line)
    print(line)
    x = line.split()
    for word in x:
        words.append(word)
print(words)
print(len(words))
