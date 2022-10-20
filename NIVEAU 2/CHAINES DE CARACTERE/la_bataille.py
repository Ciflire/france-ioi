jeu1 = input()
jeu2 = input()
n = len(jeu1)
m = len(jeu2)
eg = 0

if jeu1 == jeu2:
    print("=")

for i in range(min(n, m)):
    if jeu1[i] > jeu2[i]:
        print("2")
        break
    elif jeu2[i] > jeu1[i]:
        print("1")
        break
    else:
        eg += 1
    if eg == min(n, m):
        if n > m:
            print("1")
            break
        elif m > n:
            print("2")
            break
print(eg)
