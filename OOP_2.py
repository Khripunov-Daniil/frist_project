

def arr(lst1, lst2):
    lst3 = list(set(lst1)) + list(set(lst2))
    return [ i for i in lst3 if lst3.count(i) == i]

print(arr([6,8,6,7,3], [2,5,8,7,3]))
