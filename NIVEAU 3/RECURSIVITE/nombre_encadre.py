import sys

def rec_encadrement(x,n):
    if n == 0:
        return str(x)
    else:
        return '[' + rec_encadrement(x,n-1) + ']'

def main():
    x , n = tuple(map(int,sys.stdin.readline().split()))
    nb_encadre = rec_encadrement(x,n)
    sys.stdout.write(nb_encadre)

main()