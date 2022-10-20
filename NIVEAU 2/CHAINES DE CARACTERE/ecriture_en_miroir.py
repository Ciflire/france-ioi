nblignes = int(input())
for i in range(nblignes):
    ligne = input()
    n = len(ligne)
    for j in range(n):
        print(ligne[n-j-1], end="")
    print("")
