ch = '00010000'
n =4
def cyclisch_verschuiven(ch,n):
    lst = []
    for i in range(8):
        lst.append(ch[i])
    print(lst)
    if n > 0:   #Dit word een verplaatsing naar links
        for i in range(n):
            lst +=[lst.pop(0)]
    elif n < 0: #Dit word een verplaatsing naar rechts
        for i in range(-n):
            lst.insert(0,lst.pop(-1))
    print(lst)

cyclisch_verschuiven(ch,n)



#https://stackoverflow.com/questions/3173154/move-an-item-inside-a-list
