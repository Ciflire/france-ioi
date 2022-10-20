ligne = input()
listligne = list(ligne)
n = len(ligne)
for i in range(n):
    if listligne[i] == " ":
        listligne[i] = "_"
ligne = "".join(listligne)
print(ligne)
