n = int(input())
abscissemin = 1000000
ordonnéemin = 1000000
abscissemax = 0
ordonnéemax = 0
for i in range(n):
    Xm = int(input())
    Ym = int(input())
    if abscissemax < Xm:
        abscissemax = Xm
    if abscissemin > Xm:
        abscissemin = Xm
    if ordonnéemax < Ym:
        ordonnéemax = Ym
    if ordonnéemin > Ym:
        ordonnéemin = Ym
pérmiètre = 2 * (ordonnéemax - ordonnéemin + abscissemax - abscissemin)
print(pérmiètre)
