import re

def checkIsNone(pattern, input):
    m = re.match(pattern, input)
    return m


pattern = r'[A-Z]{1}[a-z]+\Z'
patternZipCode = r'\d{2}-\d{3}\Z'
patternPhone = r'\(\d{2}\) \d{3}-\d{2}-\d{2}\Z'

name = None
secondName = None
phone = None
zipCode = None
city = None
while not name:
    nameInput = input('Enter your name: ')
    name = checkIsNone(pattern,nameInput)
while not secondName:
    secondNameInput = input('Enter your second name: ')
    secondName = checkIsNone(pattern,secondNameInput)
while not phone:
    phoneInput = input('Enter your phone: ')
    phone = checkIsNone(patternPhone,phoneInput)
while not zipCode:
    zipCodeInput = input('Enter your ZIP Code: ')
    zipCode = checkIsNone(patternZipCode,zipCodeInput)
while not city:
    cityInput = input('Enter your city: ')
    city = checkIsNone(pattern,cityInput)
