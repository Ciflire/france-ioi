n = int(input())


def diag(g):
    dhb = 0
    dbh = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                dhb += g[i][j]
            if i + j == n-1:
                dbh += g[j][i]
    return dhb, dbh


def ligne(g, i):
    lignei = 0
    for j in range(n):
        lignei += g[i][j]
    return lignei


def colonne(g, j):
    colonnej = 0
    for i in range(n):
        colonnej += g[i][j]
    return colonnej


def liste_somme(g):
    l_val = []
    for i in range(n):
        l_val.append(ligne(g, i))
    for j in range(n):
        l_val.append(colonne(g, j))
    d1, d2 = diag(g)
    l_val.append(d1)
    l_val.append(d2)
    return l_val


def verif(l_val):
    base = l_val[0]
    for i in range(1, len(l_val)):
        if base != l_val[i]:
            return False
    return True


def rendu(l_val, g):
    if verif(l_val) and contient_tout_le_monde(g):
        print("yes")
    else:
        print("no")


def contient_tout_le_monde(g):
    l = [False] * n**2
    for i in range(n):
        for j in range(n):
            if g[i][j] <= n**2 and g[i][j] > 0:
                l[g[i][j]-1] = True
    for i in range(n**2):
        if not(l[i]):
            return False
    return True


def recupgraph(n):
    graph = [[] * n for _ in range(n)]
    for i in range(n):
        l = input().split()
        for j in range(n):
            l[j] = int(l[j])
        for j in range(n):
            graph[i].append(l[j])
    return graph


graph = recupgraph(n)

l_somme = liste_somme(graph)

rendu(l_somme, graph)
