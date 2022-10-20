debut = int(input())
fin = int(input())
nbpers = int(input())
res = 0
for i in range(nbpers):
    datearrivee = int(input())
    if (fin - datearrivee >= 0) and (debut - datearrivee) <= 0:
        res = res + 1
print(res)
