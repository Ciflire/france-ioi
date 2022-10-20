nb_livres = int(input())


def compo_liste(n):
    l = []
    for i in range(n):
        trad = str(input())
        l.append(trad.split())
    return l


def dico_inverse(l, n):
    for i in range(n):
        l[i][0], l[i][1] = l[i][1], l[i][0]
    return l


def retourne(l, n):
    for i in range(n):
        print(l[i][0], l[i][1])


liste = compo_liste(nb_livres)
inversee = dico_inverse(liste, nb_livres)
inversee.sort()
retourne(inversee, nb_livres)
