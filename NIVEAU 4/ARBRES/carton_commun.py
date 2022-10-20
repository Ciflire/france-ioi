import sys
sys.setrecursionlimit(10**6)

def fromRoot(n,a):
    if a[n-1] == 0:
        return [n]
    else:
        return fromRoot(a[n-1],a) + [n]

def firstDifferent(c1,c2):
    i = 0
    n = min(len(c1),len(c2))
    while i < n and c1[i] == c2[i]:
        i += 1
    if i == 0:
        return 0
    else:
        return c1[i-1]

def main():
    nbNoeuds = int(sys.stdin.readline())
    arbre = list(map(int,sys.stdin.readline().split()))
    nbDemandes = int(sys.stdin.readline())
    for _ in range(nbDemandes):
        noeud1,noeud2 = tuple(map(int,sys.stdin.readline().split()))
        fromRoot1 = fromRoot(noeud1,arbre)
        fromRoot2 = fromRoot(noeud2,arbre)
        print(fromRoot1,fromRoot2)
        print(firstDifferent(fromRoot1,fromRoot2))

main()


