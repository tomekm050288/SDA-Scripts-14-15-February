import random

alfabeth = []
for i in range(65, 91):
    alfabeth.append(chr(i).lower())
print(alfabeth)

scrablle = {}
for i in alfabeth:
    scrablle[i] = random.randint(1,5)
print(scrablle)

while True:
    word = input("Enter the word: ").strip()
    score = 0
    for i in word:
        score += scrablle[i]
    print("Word {} has score {}".format(word, score))
    a = input("Do you want to continue: [y/n]: ")
    if a != "y":
        break