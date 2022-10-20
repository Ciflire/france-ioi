ddeb = int(input())
dfin = int(input())
nbinv = int(input())
suspects = 0
for i in range(nbinv):
    invar = int(input())
    invdep = int(input())
    if (ddeb >= invar) and (dfin <= invdep):
        suspects += 1
    elif (ddeb <= invar) and (dfin >= invar):
        suspects += 1
    elif (ddeb <= invar) and (dfin >= invdep):
        suspects += 1
    elif (ddeb >= invar) and (ddeb <= invdep):
        suspects += 1
print(suspects)
