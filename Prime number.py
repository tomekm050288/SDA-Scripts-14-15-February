
# function to check if the number is prime

def IsPrime(number):
    lst = []
    for i in range(2,number):
        if number % i == 0:
            lst.append(i)
    if len(lst) == 0:
        print("Prime number")
    else:
        print("Non prime number")

def prime(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True
​
print(prime(13))
print(prime(8))