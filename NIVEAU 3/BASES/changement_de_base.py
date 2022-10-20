import sys


def toBaseTen(base,l):
    n = len(l)
    if n == 1:
        return l[0]
    else:
        return l[0] * (base ** (n-1)) + toBaseTen(base,l[1:])

def fromBaseTen(base,n):
    l = []
    if n == 0:
        return [0]
    while n != 0:
        l.append(n%base)
        n //= base
    return l

def main():
    baseInit, baseFinal , nbChiffres = tuple(map(int,sys.stdin.readline().split()))
    liste = list(map(int,sys.stdin.readline().split()))
    enBase10 = toBaseTen(baseInit,liste)
    enBaseFinale = fromBaseTen(baseFinal,enBase10)
    enBaseFinale = list(map(str,enBaseFinale))
    enBaseFinale.reverse()
    sys.stdout.write(" ".join(enBaseFinale))

main()