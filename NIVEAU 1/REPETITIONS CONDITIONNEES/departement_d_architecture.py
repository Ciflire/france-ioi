nbbriquesmax = int(input())
h = 1
nbbriques = 0
while nbbriquesmax > 0:
    nbbriques += h**2
    h += 1
    nbbriquesmax = nbbriquesmax - h**2
print(h-1)
print(nbbriques)
