import random

random = random.randint(1,10)
while True:
    gok = int(input('Gok welk getal het is tussen 1 en 10: '))
    if gok == random:
        print('Gefeliciteerd!\nJe hebt het juiste getal gekozen')
        break
    else:
        print('Dit is helaas niet het getal.\nProbeer opnieuw\n')
