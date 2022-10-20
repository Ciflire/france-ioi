nbJours = int(input())
res = 0
for i in range(nbJours):
    distance = int(input())
    if distance > res:
        res = distance
print(res)
