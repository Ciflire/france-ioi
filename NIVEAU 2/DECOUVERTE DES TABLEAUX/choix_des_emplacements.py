nbemp = int(input())
listemp = [0] * nbemp
emp = [0] * nbemp
for i in range(nbemp):
    listemp[i] = i + 1
for i in range(nbemp):
    tirage = int(input())
    emp[tirage] = i
for i in range(nbemp):
    print(emp[i])
