ascii_dict = {chr(i): i - 96 for i in range(97, 123)}
print(ascii_dict)


def add_letters(*letters):
    ascii_dict = {chr(i): i - 96 for i in range(97, 123)}
    rev_ascii_dict = {v: k for k, v in ascii_dict.items()}
    lst = [ascii_dict[i] for i in letters]
    if len(letters) == 0:
        return 'z'
    elif len(letters) == 1:
        return letters[0]
    elif sum(lst) <= max(ascii_dict.values()):
        return rev_ascii_dict[sum(lst)]
    else:
        return rev_ascii_dict[sum(lst) % max(ascii_dict.values())]

def add_letters(*letters):
    return chr((sum(ord(c)-96 for c in letters)-1)%26 + 97)


print(add_letters('a','b','c'))
print(add_letters("z"))
print(add_letters("a"))
print(add_letters('a','b'))
print(add_letters())
print(add_letters('y','c','b'))