def rec_dicho(x,l):
    n = len(l)
    if n == 0:
        return 0
    elif n == 1:
        if x == l[0]:
            return 1
        else:
            return 0
    else:
        def aux(a,b):
            m = (a+b)//2
            if a >= b or b > n:
                return 0
            elif x == l[m]:
                return 1
            else:
                if x > l[m]:
                    return(aux(m+1,b))
                else:
                    return(aux(a,m))
        return aux(0,n)


def main():
    n = int(input())
    l = list(map(int,input().split()))
    q = int(input())
    l.sort()
    pres = [0] * q
    for i in range(q):
       pres[i] = rec_dicho(int(input()),l)
    print("\n".join([str(i) for i in pres]))

main()