def freq(text):
    n = len(text)
    nb_occ = [0] * 26
    nb_carac = 0
    for i in range(n):
        carac = text[i]
        if carac.isalpha():
            nb_occ[ord(carac) % 65] += 1
            nb_carac += 1
    return nb_occ


def max_ind(liste):
    maxocc = 0
    maxind = 0
    for i in range(26):
        if liste[i] > maxocc:
            maxocc = liste[i]
            maxind = i
    return maxind


def decrypte(p, d):
    n = len(p)
    ligne_d = ""
    for i in range(n):
        if p[i].islower():
            rg = ord(p[i]) % 97
            rg -= d
            rg = rg % 26
            lettre = chr(rg + 97)
            ligne_d += lettre
        elif p[i].isupper():
            rg = ord(p[i]) % 65
            rg -= d
            rg = rg % 26
            lettre = chr(rg + 65)
            ligne_d += lettre
        else:
            ligne_d += p[i]
    return ligne_d


ligne_cryptee = str(input())
ligne_cryptee_maj = ligne_cryptee.upper()
liste_freq = freq(ligne_cryptee_maj)

d = max_ind(liste_freq) - 4
print(decrypte(ligne_cryptee, d))
