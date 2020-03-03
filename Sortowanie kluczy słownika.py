d = {"aaa":1, "bbb": 123, "ccc": 3223}

def sortowanie(dict, ascending = False):
    return sorted(list(dict.keys()),reverse=ascending)


print(sortowanie(d,True))


