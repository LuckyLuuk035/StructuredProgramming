def palindroom():
    var = input('vul een palindroom in: ')
    if var == var[::-1]:
        print('Dat is inderdaad een palindroom')
    else:
        print('Dit is geen palindroom')

palindroom()
#https://stackoverflow.com/questions/931092/reverse-a-string-in-python
