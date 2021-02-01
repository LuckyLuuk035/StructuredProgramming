def fibonaci(n):
    a = 0
    b = 1
    c = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    print(c)
    
    
n = int(input('vul een getal in: '))

fibonaci(n)
