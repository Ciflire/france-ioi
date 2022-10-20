nbpersonnes = int(input())
n = 1
nbmalades = 1
while nbpersonnes - nbmalades > 0:
    nbmalades += nbmalades*2
    n += 1
print(n)
