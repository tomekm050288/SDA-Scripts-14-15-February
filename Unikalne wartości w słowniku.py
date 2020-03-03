d = {"aaa":1, "bbb": 123, "ccc": 3223, "ddd" : 345, "eee" : 1, "fff" : 123}

lst = []
for key, value in d.items():
    if value not in lst:
        lst.append(value)

print(lst)

new_set = list(set(list(d.values())))
print(new_set)