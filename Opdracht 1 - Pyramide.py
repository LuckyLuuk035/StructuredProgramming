def forL(grote):
    print("U heeft de 'for' loop gekozen.")
    
    for i in range(grote):
        print('*'*i)
    for i in range(grote):
        print('*'*(grote - i))
    
def whileL(grote):
    print("U heeft de 'while' loop gekozen.")
    a = 0 
    while a <= grote:
        print('*'*a)
        a += 1
    while a != 0:
        print('*'*a)
        a -= 1

def reverseL(grote):
    print("U heeft voor de optie 'reverse' gekozen.")
    for i in range(grote):
        print('*'*(grote - i))
    for i in range(grote):
        if i >= 1:
            print('*'*(i+1))

while True:
    versie = input("De versie's zijn:\nfor\nwhile\nreverse\nVul de versie naar keuzen in: ")
    grote = int(input("Vul de grote van de pyramide in: "))
    if versie == 'for':
        forL(grote)
        break
    elif versie == 'while':
        whileL(grote)
        break
    elif versie == 'reverse':
        reverseL(grote)
        break
    else:
        print('Sorry dit was geen optie probeer opnieuw')
        continue
