def TowerOfHanoi(n , a, c, b):
    if n==1:
        print("%s -> %s" % (a,c))
        return
    TowerOfHanoi(n-a, a, b, c)
    print ("%s -> %s",(a,c))
    TowerOfHanoi(n-a, b, c, a)


def main():
    n = int(input())
    TowerOfHanoi(n,1,3,2)

main()