n = int(input())
res = 0
for i in range(n):
    habitants = int(input())
    if habitants > 10000:
        res = res + 1
print(res)
