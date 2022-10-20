import sys

def bin_to_dec(l):
    n = len(l)
    if n == 1 :
        return int(l[0])
    else:
        return int(l[0]) * (2**(n-1)) + bin_to_dec(l[1:])

def main():
    l = sys.stdin.readline()[:-1]
    l = [int(x) for x in l]
    print(bin_to_dec(l))

main()