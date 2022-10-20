def main():
    n = int(input())
    l_prod = [0] * 1000
    l_date = [0] * 1000
    pointeur = 0
    for _ in range (n):
        x,y = input().split()
        x,y = int(x), int(y)
        if y == 0:
            l_prod[pointeur+x:pointeur] = [0] * (-x)
            l_date[:pointeur+x] = l_date[-x:pointeur]
            pointeur += x
        else:
            l_prod[pointeur : pointeur + x] = [1] * x
            l_date[pointeur : pointeur + x] = [y] * x
            pointeur += x
    print(min(l_date[:pointeur]))

main()