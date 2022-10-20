import sys

def main():
    n,p = sys.stdin.readline().split()
    n,p = int(n),int(p)
    pres = [False] * p
    compteur = 1
    for i in range(p):
        x = int(sys.stdin.readline())
        if x == compteur :
            pres[x-1] = True
            while compteur < p + 1 and pres[compteur -1] :
                compteur += 1
        elif x <= p:
            pres[x-1] = True
        if compteur == n + 1:
            print("-1")
            continue
        print(compteur)
        


main()