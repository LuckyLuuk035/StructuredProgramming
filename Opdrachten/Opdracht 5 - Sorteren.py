data_list = [5,8,6,2,7,9,3,1,4]

def sorteren(lst):
    temp_list = []
    while lst:
        minimum = lst[0]
        for x in lst: 
            if x < minimum:
                minimum = x
        temp_list.append(minimum)
        lst.remove(minimum)
    lst = temp_list
    temp_list = []
    return lst

print(sorteren(data_list))


#https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
