res = 0
base = int(input())
socle = int(input())
diff = base - socle
for i in range(diff + 1):
    res = res + (base - i) * (base - i)
print(res)
