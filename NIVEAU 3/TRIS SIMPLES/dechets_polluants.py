

def conv(l):
    for i in range(len(l)):
        l[i] = int(l[i])


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    l = input().split()
    conv(l)
    l.sort()
    for i in range(1, m+1):
        print(l[-i], end=" ")


main()
