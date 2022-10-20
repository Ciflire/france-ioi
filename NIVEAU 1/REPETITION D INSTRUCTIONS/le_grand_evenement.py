from robot import *
for n in range(9):
    haut()
droite()
for i in range(8):
    if i % 2 == 1:
        for j in range(8):
            haut()
    else:
        for j in range(8):
            bas()
    droite()
for i in range(9):
    bas()
for h in range(9):
    gauche()
