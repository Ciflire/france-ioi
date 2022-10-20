def conv(l):
    for i in range(len(l)):
        l[i] = int(l[i])

def main():
    n = int(input())
    l = input().split()
    conv(l)
    l.sort()
    for i in range(n):
        print(l[i],end = " ")

main()