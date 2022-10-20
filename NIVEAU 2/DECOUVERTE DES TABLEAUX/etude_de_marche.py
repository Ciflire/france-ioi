nbproduits = int(input())
nbpersonnes = int(input())
prodlist = [0] * nbproduits
for i in range(nbpersonnes):
    prodpref = int(input())
    prodlist[prodpref] += 1
for i in range(len(prodlist)):
    print(prodlist[i])
