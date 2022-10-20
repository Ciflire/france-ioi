nbcons = int(input())
for i in range(nbcons):
    proba = 0
    taille = int(input())
    age = int(input())
    poids = int(input())
    cheval = int(input())
    brun = int(input())
    if 178 <= taille <= 182:
        proba += 1
    if age >= 34:
        proba += 1
    if poids < 70:
        proba += 1
    if cheval == 0:
        proba += 1
    if brun == 1:
        proba += 1
    if proba == 5:
        print("Très probable")
    if (proba == 3) or (proba == 4):
        print("Probable")
    if (proba == 1) or (proba == 2):
        print("Peu probable")
    if (proba == 0):
        print("Impossible")
