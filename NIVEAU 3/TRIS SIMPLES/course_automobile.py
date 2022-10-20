n = int(input())

def conv(l):
    for i in range(len(l)):
        l[i] = int(l[i])

def bubble_sort(l):
    compteur = 0
    ech = []
    for i in range (n):
        for j in range(n):
            if (l[j] == i+1):
                for k in range(j-i):
                    l[j-k] , l[j-k-1] = l[j-k-1] , l[j-k]
                    ech.append((l[j-k],l[j-k-1],))
                    compteur += 1
    return compteur , ech


def main():
    l = input().split()
    conv(l)
    compteur, l_echanges = bubble_sort(l)
    print(compteur)
    for (x, y) in l_echanges:
        print(x, y)


main()