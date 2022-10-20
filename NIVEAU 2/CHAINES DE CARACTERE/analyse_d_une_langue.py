lettrecherchee = input()
nblignes = int(input())
compteur = 0
for i in range(nblignes):
    ligne = input()
    n = len(ligne)
    for i in range(n):
        if ligne[i] == lettrecherchee:
            compteur += 1
print(compteur)
