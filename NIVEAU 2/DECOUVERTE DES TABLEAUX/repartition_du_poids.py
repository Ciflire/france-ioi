nbcharettes = int(input())
poidslist = [0] * nbcharettes
poidstotal = 0
for i in range(nbcharettes):
    poidscharettei = float(input())
    poidslist[i] = poidscharettei
for i in range(len(poidslist)):
    poidstotal += poidslist[i]
repartition = poidstotal/nbcharettes
difference = [0] * nbcharettes
for i in range(len(poidslist)):
    difference[i] = repartition - poidslist[i]
for i in range(len(difference)):
    print(difference[i])
