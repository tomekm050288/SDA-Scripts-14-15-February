def MostPopularItem(word):
    for x in word:
        dict = {x : word.count(x) for x in word}
    maxi = max(dict.values())
    mp = {}
    for key, value in dict.items():
        if value == maxi:
            mp[key] = value
    return mp

string = "aaaaaeeeeefffff"

print(MostPopularItem(string))