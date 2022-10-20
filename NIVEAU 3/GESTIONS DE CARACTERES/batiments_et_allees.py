def main():
    nom = input()
    caractere = nom[0]
    chiffre = int(input())
    alphchiffre = ord(caractere) % 64
    chiffrealph = chr(chiffre + 64)
    print(alphchiffre, end="")
    print(chiffrealph)


main()
