a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common(a,b):
    lst = []
    for i in set(a):
        if i in set(b):
            lst.append(i)
    return lst
print(common(a,b))

lst2 = [x for x in set(a) if x in set(b)]
print(lst2)

import random
lst_random = []
lst_random2 = []
for i in range(10):
    lst_random.append(random.randint(0,100))
    lst_random2.append(random.randint(0,100))
print(lst_random)
print(lst_random2)
print(common(lst_random,lst_random2))
