nblivres = int(input())
lenmax = 0
for i in range(nblivres):
    titre = input()
    if len(titre) > lenmax:
        lenmax = len(titre)
        print(titre)
