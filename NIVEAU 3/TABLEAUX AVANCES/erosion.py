h = int(input())
n, m = map(int, input().split())


def recup():
    res = []
    for i in range(n):
        liste = []
        ligne = input()
        for j in range(m):
            liste.append(ligne[j])
        res.append(liste)
    return res


image = recup()


neuman = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def voisins(i, j):
    compteur = 0
    if i == 0 or i == n-1:
        return 0
    elif j == 0 or j == m-1:
        return 0
    else:
        for (x, y) in neuman:
            if image[i+x][j+y] == '#':
                compteur += 1
        return compteur


def reperage():
    supp = []
    for i in range(n):
        for j in range(m):
            if image[i][j] == '#':
                if voisins(i, j) != 4:
                    supp.append((i, j))

    return supp


def erosion():
    a_supp = reperage()
    for (x, y) in a_supp:
        image[x][y] = '.'


def retour():
    for i in range(n):
        for j in range(m):
            print(image[i][j], end="")
        print("")


def main():
    for i in range(h):
        erosion()
    retour()


main()
