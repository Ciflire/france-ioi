n = int(input())
montee = 0
descente = 0
for i in range(n):
    denivele = int(input())
    if denivele > 0:
        montee = montee + denivele
    else:
        descente = descente - denivele
print(montee)
print(descente)
