trouver = int(input())
essais = 1
reponse = int(input())
while reponse != trouver:
    if reponse > trouver:
        print("c'est moins")
        essais += 1
    if reponse < trouver:
        print("c'est plus")
        essais += 1
    reponse = int(input())
print("Nombre d'essais nécessaires :")
print(essais)
