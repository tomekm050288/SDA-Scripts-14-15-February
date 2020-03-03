def duplicate_count(text):
    lst = []
    for letter in text.lower():
        if text.lower().count(letter) > 1:
            lst.append(letter)
    return len(set([x for x in text.lower() if text.lower().count(x) > 1]))

def duplicate_count(text):
    return len(set([x for x in text.lower() if text.lower().count(x) > 1]))



print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))
