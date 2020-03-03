import random

alfabeth = []
for i in range(65, 91):
    alfabeth.append(chr(i).lower())
print(alfabeth)

dict1 = {}
dict2 = {}
for i in range(10):
    dict1[random.choice(alfabeth)] = random.randint(1,100)
    dict2[random.choice(alfabeth)] = random.randint(1,100)
print(dict1)
print(dict2)

common_keys = [x for x in dict1.keys() if x in dict2.keys()]
print(common_keys)