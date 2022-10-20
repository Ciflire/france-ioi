nb_livres = int(input())
l = [""] * nb_livres
for i in range(nb_livres):
    livre = str(input())
    l[i] = livre
l.sort()
for i in range(nb_livres):
    print(l[i])
