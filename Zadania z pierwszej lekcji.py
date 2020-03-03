liczba = input("Podaj liczbę: ")

if int(liczba) % 2 == 0:
    print("Liczba parzysta")
print("Liczba nieparzysta")

def is_odd(number):
    if int(number) % 2 == 0:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")

name = input("Wprowadz liczbe: ")

is_odd(name)

def Fibbonacci(number):
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b


Fibonacci
n = int(input("Podaj element ciągu: "))
a=1
b=1
c=1

while n-2 > 0:
    c = a + b
    a = b
    b = c
    n-=1
print(c)

lst = [1,2,3,4,5]
del lst[2]
print(lst)

n = int(input("Wprowadź liczbę: "))

lst = []

for i in range(n):
    lst.append(input('dodaj imię: '))
print(lst)

dict = {}

# dodaj wiek osoby
for i in lst:
    dict[i] = int(input("Wprowadź wiek: "))

print(dict)

for key, value in dict.items():
    print("{} : {}".format(key,value))


while True:
    liczba = int(input("Wprowadź liczbę: "))
    if liczba % 2 == 0:
        print(liczba/2)
        continue
    elif liczba % 2 != 0 and liczba != 1:
        print(liczba*3 + 1)
        continue
    elif liczba == 1:
        print(liczba)
        break

a = "Tomasz"
print(a[::-1])


child = input("Wprowadź kod dna dziecka (5 cyfr) : ")
father1 = input("Wprowadź kod dna ojca 1 (5 cyfr): ")
father2 = input("Wprowadź kod dnia ojca 2 (5 cyfr): ")
if len(child) != len(father1) and len(child) != len(father2):
    raise Exception("Niewłaściowa długość znaków")
score1 = 0
score2 = 0
for i in range(len(child)):
    if child[i] == father1[i]:
        score1 += 1
    elif child[i] == father2[i]:
        score2 +=1
if score1 > score2:
    print("Ojciec 1 jest ojcem")
else:
    print("Ojciec 2 jest ojcem")

def isIzogram(text):
    set1 = set(text)
    if len(text) == len(set1):
        print("Izogram")
    else:
        print("To nie jest izogram")

isIzogram("Skrzynia")
























