prix = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
total = 0
for i in range(len(prix)):
    kilo = int(input())
    total += prix[i] * kilo
print(total)
