import sys

def toBaseTen(base,l):
    n = len(l)
    if n == 1:
        return l[0]
    else:
        return l[0] * (base ** (n-1)) + toBaseTen(base,l[1:])

def main():
    base, = sys.stdin.readline().split(" ")
    l = list(map(int,sys.stdin.readline().split(" ")))
    print(toBaseTen(base,l))

main()