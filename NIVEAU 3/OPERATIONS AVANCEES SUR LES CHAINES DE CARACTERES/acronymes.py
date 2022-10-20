acronyme = str(input())
nb_livres = int(input())


def normalisation(l_titre):
    for i in range(len(l_titre)):
        l_titre[i] = l_titre[i][0].upper() + l_titre[i][1:].lower()
    return l_titre


def affichage(l_titre):
    for i in range(len(l_titre)):
        print(l_titre[i], end=" ")
    print()


def convient(ac, titre):
    n = len(titre)
    m = len(ac)
    if n != m:
        return False
    else:
        for i in range(n):
            if ac[i] != titre[i][0]:
                return False
    return True


def main():
    for i in range(nb_livres):
        titre = str(input())
        titre_maj = titre.upper()
        l_titre = titre_maj.split()
        if convient(acronyme, l_titre):
            l_titre = normalisation(l_titre)
            affichage(l_titre)


main()
