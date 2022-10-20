n = int(input())


def recup(n):
    res = []
    for i in range(n):
        l = input().split()
        for j in range(n):
            l[j] = int(l[j])
        res.append(l)
    return res


plateau = recup(n)


def aux_vert(compteur, x, y):
    if compteur == 4:
        return True
    elif plateau[x][y] == plateau[x+1][y]:
        return aux_vert(compteur+1, x+1, y)
    else:
        return False


def aux_hori(compteur, x, y):
    if compteur == 4:
        return True
    elif plateau[x][y] == plateau[x][y+1]:
        return aux_hori(compteur+1, x, y+1)
    else:
        return False


def aux_dd(compteur, x, y):
    if compteur == 4:
        return True
    elif plateau[x][y] == plateau[x-1][y+1]:
        return aux_dd(compteur+1, x-1, y+1)
    else:
        return False


def aux_dg(compteur, x, y):
    if compteur == 4:
        return True
    elif plateau[x][y] == plateau[x+1][y+1]:
        return aux_dg(compteur+1, x+1, y+1)
    else:
        return False


def victoire():
    for i in range(n):
        for j in range(n):
            if plateau[i][j] == 0:
                continue
            if i <= n-5:  # vertical
                if aux_vert(0, i, j):
                    return plateau[i][j]
            if j <= n-5:  # horizontal
                if aux_hori(0, i, j):
                    return plateau[i][j]
            if i >= 4 and j <= n-5:  # diag droite
                if aux_dd(0, i, j):
                    return plateau[i][j]
            if i <= n-5 and j <= n-5:  # diag gauche
                if aux_dg(0, i, j):
                    return plateau[i][j]
    return 0


print(victoire())
