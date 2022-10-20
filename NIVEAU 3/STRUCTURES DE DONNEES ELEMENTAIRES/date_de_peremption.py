import sys

def main():
    n = int(sys.stdin.readline())
    l_date = [0] * 1000
    pointeur = 0
    for _ in range (n):
        x,y = sys.stdin.readline().split()
        x,y = int(x), int(y)
        if y == 0:
            l_date[- x  : pointeur] = l_date[:pointeur+x]
            pointeur += x
        else:
            l_date[pointeur : x] = [y] * x
            pointeur += x
    print(min(l_date[:pointeur]))

main()