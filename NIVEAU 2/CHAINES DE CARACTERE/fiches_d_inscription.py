nbauteurs = int(input())
for i in range(nbauteurs):
    prenomnom = input().split(" ")
    prenom = prenomnom[0]
    nom = prenomnom[1]
    print("{} {}".format(nom, prenom))
