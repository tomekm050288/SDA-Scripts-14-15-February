l = [1,2,3,4,5]
#lst_square = [x**2 for x in l]
dict = {}
for i in range(len(l)):
    dict[l[i]] = l[i]**2
print(dict)


dict2 = {x : x**2 for x in l}
print(dict2)
