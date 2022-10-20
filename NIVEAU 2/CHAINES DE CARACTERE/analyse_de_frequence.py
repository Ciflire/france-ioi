compteur = [0] * 100
entree = input().split(" ")
nblignes = int(entree[0])
nbmots = int(entree[1])
for i in range(nblignes):
    mot = input().split(" ")
    for j in range(nbmots):
        compteur[len(mot[j])-1] += 1
for i in range(100):
    if compteur[i] != 0:
        print(str(i+1) + " : " + str(compteur[i]))
