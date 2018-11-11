import re

patterns = [r'(kure)[a-z]*', r'(chuj)[a-z]*|(huj)[a-z]*', r'[a-z]*(kurw)[a-zćłą]*', r'[a-z]*(jeb)[a-zćłą]*', r'[a-z]*(pierda)[a-zćłą]*',
            r'[a-z]*(pierdo)[a-złćą]*', r'(kutas)[a-zó]*', r'(wypier)[a-zćłą]*', r'(zapiep)[a-zćłą]*', r'(wypieprz)[a-zćł]*',
            r'[a-z]*(pieprz)[a-zćłą]*', r'[a-z]*(sukinsyn)[a-z]*', r'[a-z]*(pizd)[a-zś]*', r'[a-z]*(dup)[a-z]*', r'[a-z]*(cip)[a-z]*']
def checkIsBadWord(input):
    newLine = input
    for pattern in patterns:
        newLine = re.sub(pattern, '---', newLine)
    return newLine

f2 = 'f2.txt'
fileSave = open(f2,'w', encoding='utf-8')

f = 'f.txt'
with open(f, 'r+', encoding='utf-8') as file:
    for line in file:

        newLine = checkIsBadWord(line)
        fileSave.write(newLine)