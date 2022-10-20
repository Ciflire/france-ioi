def convertion(nom):
    n = len(nom)
    res = [0] * n
    for i in range(n):
        res[i] = ord(nom[i]) % 65
    return res


def somme_nombre(entier):
    res = 0
    while entier > 0:
        res += entier % 10
        entier = entier//10
    if res >= 10:
        return somme_nombre(res)
    else:
        return res


def somme_lettre(liste_nom):
    n = len(liste_nom)
    res = 0
    for i in range(n):
        res += liste_nom[i]
    if res >= 10:
        return somme_nombre(res)
    else:
        return res


def nombre_d_amour(nom):
    res = somme_lettre(convertion(nom))
    return res


noms = str(input())
nom1, nom2 = noms.split()
print(nombre_d_amour(nom1), nombre_d_amour(nom2), sep=" ")
