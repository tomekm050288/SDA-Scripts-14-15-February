import random
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)

def convert(lst):
    lst2 = []
    for i in range(0,len(lst)-1,2):
        lst2.append(sorted(lst,reverse=True)[i])
    return lst2

print(convert(lst))

def convert2(lst):
    return sorted(lst,reverse=True)[::2]

print(convert2(lst))