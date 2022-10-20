from copy import deepcopy
import sys


def main():
    tailleListe = int(sys.stdin.readline())
    listeNb = list(map(int,sys.stdin.readline().split()))
    sup = 0
    somme = 0
    for x in listeNb:
        somme += x
        if somme > sup :
            sup = deepcopy(somme)
        elif somme < 0 :
            somme = 0
    print(sup)


main()