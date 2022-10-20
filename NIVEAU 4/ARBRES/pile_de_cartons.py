import sys

def parcoursArbre(node,a):
    l_fils = a[node]
    if len(l_fils) == 0:
        sys.stdout.write("R %i\n" % node)
    else:
        for x in l_fils:
            sys.stdout.write("A %i\n" % x)
            parcoursArbre(x,a)
        sys.stdout.write("R %i\n" % node)

def main():
    n = int(sys.stdin.readline())
    arbre = [[]] * (n+1)
    for i in range(n+1):
        arbre[i] = list(map(int,sys.stdin.readline().split()))[1:]
    for x in arbre[0]:
        sys.stdout.write("A %i\n" % x)
        parcoursArbre(x,arbre)

main()