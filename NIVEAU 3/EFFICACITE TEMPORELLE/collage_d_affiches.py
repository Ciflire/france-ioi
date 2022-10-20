import sys
from copy import deepcopy

def main():
    n = int(sys.stdin.readline())
    compteur = 0
    p = [0] * 100000
    for _ in range(n):
        l = sys.stdin.readline()
        if l[0] == 'Q':
            print(compteur)
        elif l[0] == 'C':
            car , taille = l.split()
            taille = int(taille)
            if compteur == 0:
                p[0] = deepcopy(taille)
                compteur += 1
                continue
            while p[compteur-1] <= taille and compteur > 0:
                compteur -= 1
            p[compteur] = deepcopy(taille)
            compteur += 1

main()