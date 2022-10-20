def main():
    n = int(input())
    l = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        x,y = tuple(map(int,input().split()))
        l[x] += y
    print("\n".join([str(x) for x in l]))

main()