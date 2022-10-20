from copy import deepcopy
import sys

def main():
    k,n = tuple(map(int,sys.stdin.readline().split()))
    maxi = 0
    ind = 0
    riviere = list(map(int,sys.stdin.readline().split()))
    for i in range(k):
        ind += riviere[i]
    for i in range (n-k):
        ind += riviere[i+k]
        ind -= riviere[i]
        if ind > maxi:
           maxi = deepcopy(ind)
    sys.stdout.write(maxi)

main()