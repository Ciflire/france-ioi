code1 = 4242
code2 = 2121


def entrercode1():
    tentative = 0
    while tentative != code1:
        print("Entrez le code :")
        tentative = int(input())


def entrercode2():
    tentative = 0
    while tentative != code2:
        print("Entrez le code :")
        tentative = int(input())


entrercode1()
print("Premier code bon.")
entrercode2()
print("Bravo.")
