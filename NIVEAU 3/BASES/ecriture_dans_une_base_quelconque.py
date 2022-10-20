import sys

def main():
    n , base = tuple(map(int,sys.stdin.readline().split()))
    l = []
    if n == 0:
        print('0')
    while n != 0:
        l.append(n%base)
        n //= base
    l = list(map(str,l))
    l.reverse()
    sys.stdout.write("%s\n" % len(l))
    sys.stdout.write(" ".join(l))    

main()