titre = input()
auteur = input()
for i in range(len(titre)):
    if titre[i] == "A" or titre[i] == "E" or titre[i] == "I" or titre[i] == "O" or titre[i] == "U" or titre[i] == "Y" or titre[i] == " ":
        print("", end="")
    else:
        print(titre[i], end="")
print("")
for i in range(len(auteur)):
    if auteur[i] == "A" or auteur[i] == "E" or auteur[i] == "I" or auteur[i] == "O" or auteur[i] == "U" or auteur[i] == "Y" or auteur[i] == " ":
        print("", end="")
    else:
        print(auteur[i], end="")
