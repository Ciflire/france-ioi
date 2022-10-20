def main():
    n = int(input())
    l = list(map(int,input().split()))
    l_passages = [0] * 1000001
    for i in range(n):
        l_passages[l[i]] +=1
        if l_passages[l[i]] >1:
            print(l[i])
            return
    print("-1")


main()