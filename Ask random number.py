import random
random_number = str(random.randint(1000,10000))
print(random_number)

while True:
    cows = 0
    bulls = 0
    print("Play a game - Ask random numer!")
    user_number = input("Enter the number 4 digits: ")
    for i in range(len(user_number)):
        if user_number[i] == random_number[i]:
            cows += 1
        elif (user_number[i] != random_number[i]) and user_number[i] in random_number:
            bulls += 1

    print("Your score: \nbulls : {} \ncows : {}". format(bulls, cows))
    break





