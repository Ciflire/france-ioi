import sys


def main():
    plateau = [[0] * 101 for _ in range (101)]
    n = int(input())
    liste = [None] * n
    compteur = 0
    for i in range(n):
        x,y = sys.stdin.readline().split()
        x,y = int(x), int(y)
        plateau[x][y] = 1
        liste[i] = (x,y)
    for i in range(n-1):
        x1, y1 = liste[i]
        for j in range(i+1,n):
            sum1, sum2 = 0, 0
            x2, y2 = liste[j]
            sum1 = x1 + x2
            sum2 = y1 + y2
            if sum1%2 == 0 and sum2 % 2 == 0:
                if plateau[sum1//2][sum2//2] == 1:
                    plateau[sum1//2][sum2//2] = 0
                    compteur +=1
    print(compteur)

main()
