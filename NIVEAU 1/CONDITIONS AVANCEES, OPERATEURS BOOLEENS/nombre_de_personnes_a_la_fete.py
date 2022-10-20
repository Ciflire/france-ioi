nbpersonnes = int(input())
res = 0
max = 0
for i in range(2*nbpersonnes):
    if int(input()) > 0:
        res += 1
    else:
        res += -1
    if res > max:
        max = res
print(max)
