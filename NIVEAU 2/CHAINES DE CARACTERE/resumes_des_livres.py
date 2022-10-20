nblivres = int(input())
longueurmin = int(input())
for i in range(nblivres):
    titre = input()
    resume = input()
    if len(resume) < longueurmin:
        print(titre)
