nbplaces = int(input())
nbchangements = int(input())
places = [0] * nbplaces
for i in range(nbplaces):
    places[i] = int(input())
for i in range(nbchangements):
    position1 = int(input())
    position2 = int(input())
    places[position1], places[position2] = places[position2], places[position1]
for i in range(nbplaces):
    print(places[i])
