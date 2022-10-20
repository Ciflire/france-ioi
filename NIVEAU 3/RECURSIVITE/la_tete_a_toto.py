import sys

def rec_toto(n):
    if n == 0 :
        return "0"
    else:
        return "(%s + %s)" % (rec_toto(n-1),rec_toto(n-1))

def main():
    n = int(sys.stdin.readline())
    print("0 = "+rec_toto(n))

main()