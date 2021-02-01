text = input('Geef een text: ')
rotatie = int(input('Geef een rotatie: '))
new_text = ''

for i in text:
    edit = ord(i) + rotatie
    new_text = new_text + chr(edit)
print(new_text)


#https://inventwithpython.com/chapter14.html
