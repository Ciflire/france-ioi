import sys

def valide(noeud,masque):
    noeud = str(noeud)
    lenNoeud = len(noeud)
    lenMasque = len(masque)
    if lenNoeud != lenMasque:
        return False
    for i in range(lenMasque):
        if masque[lenMasque-1-i] == '?':
            continue
        elif masque[lenMasque-1-i] != noeud[lenMasque-1-i]:
            return False
    return True

def main():
    n = int(sys.stdin.readline())
    l_fathers = list(map(int,sys.stdin.readline().split()))
    l_fils = [[]] * (n+1)
    masque = input()
    lPotentiels = []
    for noeud in range(n):
        fatherOfNoeud = l_fathers[noeud] 
        l_fils[fatherOfNoeud] = l_fils[fatherOfNoeud] + [noeud+1]
    parcours = [0]
    print(masque)
    for i in range(n+1):
        parcours += l_fils[parcours[i]]
    for x in parcours[1:]:
        if valide(x,masque):
            sys.stdout.write("%i" %x)
            sys.stdout.write(" ")



main()
