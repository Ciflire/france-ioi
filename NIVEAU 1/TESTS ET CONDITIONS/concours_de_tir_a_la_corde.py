# définitions des variables
nb = int(input())
eq1 = 0
eq2 = 0
# boucle définir les masses de équipes
for i in range(2*nb):
    masse = int(input())
    if i % 2 == 0:
        eq1 = eq1 + masse
    else:
        eq2 = eq2 + masse
# qui est le plus lourd
if eq2 < eq1:
    print('''L'équipe 1 a un avantage''')
else:
    print('''L'équipe 2 a un avantage''')
# print les masses
print("Poids total pour l'équipe 1 : ", eq1)
print("Poids total pour l'équipe 2 : ", eq2)
