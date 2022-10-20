nbmes = int(input())
tmin = int(input())
tmax = int(input())
n = 1
alerte = 0
while (alerte != 1) and (n <= nbmes):
    mesure = int(input())
    if tmin <= mesure <= tmax:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        alerte += 1
    n += 1
