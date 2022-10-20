nbpart = int(input())
lnb = [0] * nbpart
for i in range(nbpart):
    lnb[i] = int(input())
lnb.sort()
for i in range(nbpart//2):
    print("{} {}".format(str(lnb[i]), str(lnb[nbpart-i-1])))
