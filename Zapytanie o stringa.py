def conver(word):
    lst = word.split(" ")[::-1]
    result = ""
    for i in lst:
        result += i + " "
    return result.strip()

long_string = input("Enter the long string: ")

print(conver(long_string))
