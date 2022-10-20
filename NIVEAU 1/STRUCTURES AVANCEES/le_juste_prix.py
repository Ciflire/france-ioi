n = int(input())
pos = 0
meilleurprix = 1000000
for i in range(n):
    prix = int(input())
    if meilleurprix >= prix:
        meilleurprix = prix
        pos = i+1
print(pos)
