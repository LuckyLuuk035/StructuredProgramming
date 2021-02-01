s1 = input('Geef een string: ')
s2 = input('Geef een string: ')

lst1 = []
lst2 = []
for i in range(len(s1)):
    lst1.append(s1[i])
for i in range(len(s2)):
    lst2.append(s2[i])

if len(s1) > len(s2):
    grootste = len(s1)
elif len(s2) > len(s1):
    grootste = len(s2)
else:
    grootste = len(s1)

a = 1
while True:
    if lst1[a] != lst2[a]:
        TheIndex = str(a)
        break
    a+=1

print('Het eerste verschil zit op index: '+ TheIndex)
    
##bron(nen):---------------------------------------------------------
##https://stackoverflow.com/questions/8545492/find-the-position-of-difference-between-two-strings
##-------------------------------------------------------------------
