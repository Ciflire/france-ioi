pos = int(input())
nbvillages = int(input())
res = 0
for i in range(nbvillages):
    posv = int(input())
    if 50 >= posv-pos >= -50:
        res = res + 1
    else:
        res = res
print(res)
