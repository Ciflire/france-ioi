nbdep = int(input())
dep = [0] * nbdep
retour = [0] * nbdep
for i in range(nbdep):
    dep[i] = int(input())
dep.reverse()
for i in range(nbdep):
    if dep[i] == 1:
        retour[i] = 2
    elif dep[i] == 2:
        retour[i] = 1
    elif dep[i] == 4:
        retour[i] = 5
    elif dep[i] == 5:
        retour[i] = 4
    else:
        retour[i] = 3
for i in range(nbdep):
    print(retour[i])
