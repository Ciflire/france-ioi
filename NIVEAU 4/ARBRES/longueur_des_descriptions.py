from copy import deepcopy
import sys

def profondeurNoeud(x,a):
    if a[x] == 0 :
        return 1
    else:
        return 1 + profondeurNoeud(a[x],a)

def main():
    n = int(sys.stdin.readline())
    l_fathers = list(map(int,sys.stdin.readline().split()))
    l_fils = [[]] * (n+1)
    hauteur = 1
    for noeud in range(n):
        fatherOfNoeud = l_fathers[noeud] 
        l_fils[fatherOfNoeud] = l_fils[fatherOfNoeud] + [noeud+1]
    for noeud in range(1,n+1):
        print(noeud,l_fils[noeud])
        if len(l_fils[noeud]) == 0:
            niveau = profondeurNoeud(noeud-1,l_fathers)
            print(noeud-1)
            if niveau > hauteur:
                hauteur = deepcopy(niveau)
    sys.stdout.write(str(hauteur))

main()