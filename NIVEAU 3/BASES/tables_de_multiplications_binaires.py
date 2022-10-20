def toBin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return str(n%2) + toBin(n//2)


def main():
    n = int(input())
    tableauDec = [[0] for _ in range(n)]
    tableauBin = [[0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tableauDec[i][j] = (i+1)(j+1)
            tableauBin[i][j] = toBin(tableauDec[i][j])
            print(tableauBin[i][j], end = " ")
        print("")

main()