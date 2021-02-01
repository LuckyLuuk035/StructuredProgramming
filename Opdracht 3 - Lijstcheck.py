lst1 = [3,6,3,4,9,2,7,5,3,2,6]
lst2 = [1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0]
def count(lst):
    #Om in de lijstcheck() gebruik te kunnen maken van count heb ik de input weg gehaald.
    #Maar deze kan als nodig weer terug gezet worden om los gebruik te maken van count()
    #x = input('Vul getal in: ')
    x = 0
    a = 0
    for i in lst:
        if int(x) == int(i):
            a += 1
    #Dit stuk is ook toegevoegd voor de lijstcheck
    x = 1
    b = 0
    for i in lst:
        if int(x) == int(i):
            b += 1
        
    #print("het getal "+str(x)+" komt "+str(a)+"x in de lijst voor.")
    return a, b

def verschil():
    a = 0
    g2 = 0
    for i in lst:
        if lst[a] > lst[a-1]:
            g1 = lst[a]
            k1 = lst[a-1]
        elif lst[a] < lst[a-1]:
            g1 = lst[a-1]
            k1 = lst[a]
        k2 = g1-k1
        if k2 > g2:
            g2 = k2
        a += 1
    print("het grootste verschil tussen twee op een volgende getallen is "+str(g2))

def lijstcheck():
    
    if count(lst2)[0] < count(lst2)[1] and count(lst2)[0] <= 12:
        result = True
    else:
        result = False
    return result
    
print(lijstcheck())
