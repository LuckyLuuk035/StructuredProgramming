def fibonacci(n):
    lst = [0,1]+([0]*(n-1))
    for i in range(2, n+1):
        lst[i] = lst[i-2] + lst[i-1]
    return lst[n]
    
n = int(input('vul een getal in: '))

print(fibonacci(n))
