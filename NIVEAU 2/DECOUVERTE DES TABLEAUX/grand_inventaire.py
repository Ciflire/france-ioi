nboperations = int(input())
stock = [0] * 10
for i in range(nboperations):
    nstock = int(input())
    modif = int(input())
    stock[nstock-1] = stock[nstock-1] + modif
for i in range(len(stock)):
    print(stock[i])
