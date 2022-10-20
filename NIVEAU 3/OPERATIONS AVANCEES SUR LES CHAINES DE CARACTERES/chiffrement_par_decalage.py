def decrypte_pp(p, np):
    n = len(p)
    ligne_d = ""
    for i in range(n):
        if p[i].islower():
            rg = ord(p[i]) % 97
            rg -= 3*np
            rg = rg % 26
            lettre = chr(rg + 97)
            ligne_d += lettre
        elif p[i].isupper():
            rg = ord(p[i]) % 65
            rg -= 3*np
            rg = rg % 26
            lettre = chr(rg + 65)
            ligne_d += lettre
        else:
            ligne_d += p[i]
    return ligne_d


def decrypte_pi(p, np):
    n = len(p)
    ligne_d = ""
    for i in range(n):
        if p[i].islower():
            rg = ord(p[i]) % 97
            rg -= -5*np
            rg = rg % 26
            lettre = chr(rg + 97)
            ligne_d += lettre
        elif p[i].isupper():
            rg = ord(p[i]) % 65
            rg -= -5*np
            rg = rg % 26
            lettre = chr(rg + 65)
            ligne_d += lettre
        else:
            ligne_d += p[i]
    return ligne_d


nb_pages = int(input())


def main(n):
    for i in range(2, n+1):
        if i % 2 == 0:
            ligne = str(input())
            print(decrypte_pp(ligne, i))
        else:
            ligne = str(input())
            print(decrypte_pi(ligne, i))


main(nb_pages)
