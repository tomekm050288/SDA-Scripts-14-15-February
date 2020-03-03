from itertools import permutations


def next_bigger(n):
    if n < 11:
        return -1
    gen_perm = (int(''.join(map(str,x))) for x in permutations([int(x) for x in str(n)]))
    try:
        for i in gen_perm:     
            if i == n:
                a = next(gen_perm)
                if a < n:
                    return -1
                else:
                    while a <= i:
                        a = next(gen_perm)
                    return a
    except StopIteration:
        return -1



print(next_bigger(4567889))


#gen_perm = (int(''.join(map(str,x))) for x in permutations([int(x) for x in str(n)]))




