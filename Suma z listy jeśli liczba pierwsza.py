import random

# lst = [random.randint(1,100) for x in range(10)]
# print(lst)
lst2 = [1,2,3,4,5,6,7]

def prime(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

print(prime(17))
print(prime(8))


def sum_prime(lst):
    return sum([x for x in lst if prime(x)])


print(lst2)
print(sum_prime(lst2))