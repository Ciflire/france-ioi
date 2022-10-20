nbhab = int(input())
l = [0] * nbhab
for i in range(nbhab):
    l[i] = int(input())
l.sort()
l_len = len(l)
if l_len % 2 == 0:
    print((l[(l_len-1)//2] + l[(l_len+1)//2]) / 2.0)
if l_len % 2 != 0:
    print(l[(l_len-1)//2])
