import sys

def dicho(x,l,inf,sup):
    while sup-inf >2:
        mid = (sup+inf)//2
        if x > l[mid]:
            inf = mid 
        elif x < l[mid]:
            sup = mid 
    if abs(x - l[sup]) <= abs(x-l[inf]):
        return l[sup]
    else:
        return l[inf]


def rec_dicho(x, l):
    n = len(l)
    if n == 1:
        return l[0]
    elif n == 2:
        if abs(x - l[0]) <= abs(x-l[1]):
            return l[0]
        else:
            return l[1]
    else:
        if x == l[n//2]:
            return l[n//2]
        elif x < l[n//2]:
            return rec_dicho(x,l[:n//2])
        else:
            return rec_dicho(x,l[n//2:])


def main():
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    l.sort()
    pres = [0] * q
    for i in range(q):
        pres[i] = dicho(int(input()), l)
    print("\n".join([str(i) for i in pres]))

main()