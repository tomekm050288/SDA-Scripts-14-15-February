ciag_znakow = input("Enter string of characters: ")

def counter_for_letter(letter):
    counter = 0
    for i in ciag_znakow:
        if i == letter:
            counter += 1
    return counter

print(counter_for_letter("a"))

for i in ciag_znakow:
    dict = {x : ciag_znakow.count(x) for x in ciag_znakow}
print(dict)


dict3 = {}
for i in ciag_znakow:
    if i not in dict3.keys():
        dict3[i] = 1
    else:
        dict3[i] += 1

print(dict3)







