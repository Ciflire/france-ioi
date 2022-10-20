def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(str(input()))
    l.sort()
    for i in range(n):
        print(l[i])

main()