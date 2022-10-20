nb_livres = int(input())


def compo_liste(n):
    liste = [""]*n
    for i in range(n):
        liste[i] = str(input())
    return liste


liste = compo_liste(nb_livres)


def main():
    dernier_livre = liste[0]
    for i in range(nb_livres):
        if dernier_livre <= liste[i]:
            print(liste[i])
            dernier_livre = liste[i]


main()
