taxeact = float(input())
taxenew = float(input())
prixact = float(input())
prixbase = prixact/(1+(taxeact/100))
prixnew = round((prixbase + prixbase*(taxenew/100))*100)/100
print(prixnew)
