def X(n):
    for i in range(n):
        print("X", end="")


def hashtag(n, m):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(m):
                print("#", end="")
        else:
            for j in range(m):
                if j == 0 or j == m-1:
                    print("#", end="")
                else:
                    print(" ", end="")
        print("")


def triangle(n):
    for i in range(n):
        if i != n - 1:
            for j in range(i+1):
                if j == 0 or j == i:
                    print("@", end="")
                else:
                    print(" ", end="")
            print("")
        elif i == n - 1:
            for j in range(n):
                print("@", end="")


nbX = int(input())
lignehashtag = int(input())
colonneshashtag = int(input())
lignetri = int(input())

X(nbX)
print("")
print("")
hashtag(lignehashtag, colonneshashtag)
print("")
triangle(lignetri)
