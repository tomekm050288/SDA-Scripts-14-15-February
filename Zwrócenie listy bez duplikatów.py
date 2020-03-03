a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lst2 = list(set(a))
print(lst2)


def non_duplicates(lst):
    lst_without_dup = []
    for i in lst:
        if i not in lst_without_dup:
            lst_without_dup.append(i)
    return lst_without_dup

print(non_duplicates(a))