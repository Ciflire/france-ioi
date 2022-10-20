import sys

def main():
    n = int(sys.stdin.readline())
    puiss = 0
    while 2**puiss <= n :
        puiss += 1
    print(2**(puiss-1))

main()