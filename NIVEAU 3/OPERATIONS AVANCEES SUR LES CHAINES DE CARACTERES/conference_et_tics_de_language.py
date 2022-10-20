mot = str(input())
mot_maj = mot.upper()
discours = str(input())
discours_maj = discours.upper()
l_discours = discours_maj.split()
compteur = 0
for i in range(len(l_discours)):
    if l_discours[i] == mot_maj:
        compteur += 1
print(compteur)
