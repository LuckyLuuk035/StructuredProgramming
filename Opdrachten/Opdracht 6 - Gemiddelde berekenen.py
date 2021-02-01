data_list = [5,8,6,2,7,9,3,1,4]
lst_list = [[5,8,6],[2,7,9],[3,1,4]]

def gemiddelde(lst):
    getal = 0
    for i in lst:
        getal += i
    gemiddelde = getal / len(lst)
    return gemiddelde

def gemiddeldelst(lst):
    getal = 0
    lengte = 0
    for i in lst:
        for a in lst[lst.index(i)]:
            getal += a
            lengte += 1
            
    gemiddelde = getal / lengte
    return gemiddelde

print(gemiddeldelst(lst_list))

