nb_livres = int(input())
l = []
for i in range(nb_livres):
    livre = str(input())
    l.append(livre)
for i in range(nb_livres):
    print(l[-i-1])
