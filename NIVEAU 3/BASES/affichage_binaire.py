import sys

def main():
    n = int(sys.stdin.readline())
    l = []
    if n == 0:
        print('0')
    while n != 0:
        l.append(n%2)
        n //= 2
    l = list(map(str,l))
    l.reverse()
    sys.stdout.write("".join(l))

main()