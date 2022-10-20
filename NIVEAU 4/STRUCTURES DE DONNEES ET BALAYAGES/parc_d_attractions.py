import sys


#V1
''' 
def sum(l,i,f):
    res = 0
    for j in range(i-1,f):
        res += l[j]
    return res


def main():
    nbJours , nbPeriodes = tuple(map(int,sys.stdin.readline().split()))
    lVisiteur = list(map(int,sys.stdin.readline().split()))
    for periode in range(nbPeriodes):
        dDeb , dFin = tuple(map(int,sys.stdin.readline().split()))
        sys.stdout.write("%i" % sum(lVisiteur,dDeb,dFin))
        sys.stdout.write(" ")

main()
'''

#V2
def tabCumu(l):
    n = len(l)
    tab = [0] * (n+1)
    res = 0
    for i in range(1,n+1):
        res += l[i-1]
        tab[i] = res
    return tab

def main():
    nbJours , nbPeriodes = tuple(map(int,sys.stdin.readline().split()))
    lVisiteur = list(map(int,sys.stdin.readline().split()))
    tabEcc = tabCumu(lVisiteur)
    for periode in range(nbPeriodes):
        dDeb , dFin = tuple(map(int,sys.stdin.readline().split()))
        sys.stdout.write("%i\n" % tabEcc[dFin]-tabEcc[dDeb-1])
    return

main()