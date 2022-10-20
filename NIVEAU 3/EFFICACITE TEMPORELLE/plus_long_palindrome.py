from copy import deepcopy
import sys

def plusGrosPalindromeLocal(l,ind):
    dec = 0
    n = len(l)
    pMaxi = 1
    while ind-dec >= 0 and ind+dec < n and l[ind-dec] == l[ind+dec]:
        dec += 1
    taille = (dec-1)*2
    if taille > pMaxi:
        pMaxi = deepcopy(taille)
    dec = 0
    while ind-dec >= 0 and ind+dec < n-1 and l[ind-dec] == l[ind+dec]:
        dec += 1
    taille = dec*2 -1
    if taille > pMaxi:
        pMaxi = deepcopy(taille)
    return pMaxi

def main():
    l = sys.stdin.readline()
    n = len(l)
    for i in range(n):
        p_max = plusGrosPalindromeLocal(l,i)
    print(p_max)

main()
