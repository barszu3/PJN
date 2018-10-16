import csv
import re


def checkIsNone(pattern, input):
    m = re.match(pattern, input)
    return m

file = 'plik.csv'
decision = True
pattern = r'.*'
patternSecond = r'(-[1-9]+)|(\d+)'
with open(file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        x = checkIsNone(pattern,row[0])
        y = checkIsNone(patternSecond,row[1])
        z = checkIsNone(patternSecond, row[2])
        if len(row) > 3:
            decision = False
            break
        if not x or not y or not z:
            decision = False
            break
if decision == False:
    print('Plik niepoprawny')