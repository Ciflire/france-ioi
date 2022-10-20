n, m = input().split()
n, m = int(n), int(m)

graph = [["."] * m for _ in range(n)]


def main():
    nb_rect = int(input())
    for i in range(nb_rect):
        imin, jmin, imax, jmax, car = input().split()
        imin, jmin, imax, jmax, car = int(imin), int(
            jmin), int(imax), int(jmax), str(car)
        for i in range(imin, imax+1):
            for j in range(jmin, jmax+1):
                graph[i][j] = car


def affiche(g):
    for i in range(n):
        for j in range(m):
            print(g[i][j], end="")
        print()


main()
affiche(graph)
