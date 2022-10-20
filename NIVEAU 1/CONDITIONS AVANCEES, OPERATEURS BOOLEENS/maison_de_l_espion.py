absmin = int(input())
absmax = int(input())
ordmin = int(input())
ordmax = int(input())
nbmaisons = int(input())
res = 0
for i in range(nbmaisons):
    abs = int(input())
    ord = int(input())
    if (abs >= absmin) and (abs <= absmax):
        if (ord >= ordmin) and (ord <= ordmax):
            res = res + 1
print(res)
