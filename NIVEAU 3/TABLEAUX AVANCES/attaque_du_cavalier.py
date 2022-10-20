def move_c(x, y):
    return [[x-2, y-1], [x-2, y+1], [x-1, y+2], [x+1, y+2], [x+2, y-1], [x+2, y+1], [x-1, y-2, ], [x+1, y-2]]


def recupgraph():
    graph = []
    for i in range(8):
        l = input()
        graph.append(l)
    return graph


def pos_c(g):
    l = []
    for i in range(8):
        for j in range(8):
            ligne = g[i]
            if ligne[j] == 'C':
                l.append([i, j])
    return l


def atk(g):
    pos_cavalier = pos_c(g)
    for i in range(len(pos_cavalier)):
        move = move_c(pos_cavalier[i][0], pos_cavalier[i][1])
        for x, y in move:
            if 0 <= x <= 7 and 0 <= y <= 7:
                if g[x][y].islower():
                    return True
    return False


def result(g):
    if atk(g):
        print("yes")
    else:
        print("no")


graph = recupgraph()
result(graph)
