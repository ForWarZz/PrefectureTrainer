import csv
import random

def question(n):
    return [question_nom_dpt, question_prefecture_dpt][n]
    
def question_nom_dpt():
    dpt = random_dpt()

    dpt_name = dpt[2]
    dpt_prefecture = dpt[3]
    
    result = input(f"Quel est le nom du département de la préfécture {dpt_prefecture} ? \n")

    if result.lower() == dpt_name.lower():
        print("Bonne réponse !")
    else:
        print(f"Mauvaise réponse : {dpt_prefecture} -> {dpt_name}")

def question_prefecture_dpt():
    dpt = random_dpt()

    dpt_prefecture = dpt[3]
    dpt_name = dpt[2]
    
    result = input(f"Quel est le nom de la préfécture -> {dpt_name} ? \n")

    if result.lower() == dpt_prefecture.lower():
        print("Bonne réponse !")
    else:
        print(f"Mauvaise réponse : {dpt_name} -> {dpt_prefecture}")

def random_dpt():
    random_number = random.randint(0, len(dpts) -1)
    return dpts[random_number]

dpts = []

with open('departement.csv', encoding='utf-8') as file:
    dpts = list(csv.reader(file))[1::]

while True:
    random_question = random.randint(0, 1)
    question(random_question)()
