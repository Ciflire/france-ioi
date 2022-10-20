def motif(l, L, lettre):
    for i in range(l):
        for j in range(L):
            print(lettre, end="")
        print("")


l = int(input())
L = int(input())
lettre = input()
motif(l, L, lettre)
