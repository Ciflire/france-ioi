nbjetons = int(input())
for i in range(nbjetons):
    absc = int(input())
    ordo = int(input())
    if ((0 <= ordo <= 10) and (0 <= absc <= 90)) or ((55 <= ordo <= 60) and (0 <= absc <= 90)) or ((0 <= absc <= 10) and (0 <= ordo <= 70)) or ((85 <= absc <= 90) and (0 <= ordo <= 70)) or ((25 <= absc <= 50) and (20 <= ordo <= 45)) or ((60 <= ordo <= 70) and ((10 <= absc <= 15) or (45 <= absc <= 60))):
        print("Dans une zone jaune")
    elif (10 <= ordo <= 20 and 10 <= absc <= 85) or (45 <= ordo <= 55 and 10 <= absc <= 85) or (20 <= ordo <= 45 and (10 <= absc <= 25 or 50 <= absc <= 85)):
        print("Dans une zone bleue")
    elif (60 <= ordo <= 70 and (15 <= absc <= 45 or 60 <= absc <= 85)):
        print("Dans une zone rouge")
    else:
        print("En dehors de la feuille")
