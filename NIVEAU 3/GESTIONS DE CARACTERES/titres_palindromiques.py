def palindrome(text):
    n = len(text)
    indg = 0
    indd = -1
    while indg < n//2 and indd >= -n//2:
        if ord(text[indg]) == 32:  # décalage si espace
            indg += 1
        if ord(text[indd]) == 32:  # idem
            indd -= 1
        if text[indg] != text[indd]:  # comparaison entre premier et dernier elt
            return False
        indg += 1
        indd -= 1
    return True


def res(n):
    for i in range(n):
        livre = str(input())
        livre_maj = livre.upper()
        if palindrome(livre_maj):
            print(livre)


nb_livres = int(input())
res(nb_livres)
