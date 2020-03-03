lst = ['A','C','G','T']

# funcka budująca kod DNA dziecka i ojca
import random

def DNA(lst, long_of_dna):
    dna_code = ""
    for i in range(long_of_dna):
        dna_code += random.choice(lst)
    return dna_code

#print(DNA(lst,10))
# child = DNA(lst,10)
# father1 = DNA(lst,10)
# father2= DNA(lst,10)
# print(child)


# def checker_of_dna(child, father1, father2):
#     score_1 = 0
#     score_2 = 0
#     for i in range(len(child)):
#         if child[i] == father1[i]:
#             score_1 += 1
#         elif child[i] == father2[i]:
#             score_2 += 1
#     return ("Person 1 is father, score: {}, dna: {}".format(score_1,father1)) if score_1 > score_2 else ("Person 2 is father, score: {}, dna: {}".format(score_2,father2))
#
# print(checker_of_dna(child, father1, father2))


# dla n ojców

def checker_of_dna(child, father):
    score = 0
    for i in range(len(child)):
        if child[i] == father[i]:
            score += 1
    return score


child2 = DNA(lst,10)
print("DNA of child is: ",child2)

n = int(input("Enter number of potential fathers: "))
no_person = 1
no_for_father = 1
highest_score = 0

while no_person <= n:
    father = DNA(lst,10)
    print("DNA of person no {} is {}".format(no_person,father))
    result = checker_of_dna(child2, father)
    if result > highest_score:
        highest_score = result
        no_for_father = no_person
    no_person += 1

print("Person no {} is father with highest score {}".format(no_for_father,highest_score))