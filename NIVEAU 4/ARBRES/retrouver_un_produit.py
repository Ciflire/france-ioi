import sys



def main():
    nb_products = int(sys.stdin.readline())
    l_fathers = list(map(int,sys.stdin.readline().split()))
    nb_wanted = int(sys.stdin.readline())
    l_wanted = list(map(int,sys.stdin.readline().split()))    
    for x in l_wanted:
        path = [str(x)]
        while l_fathers[x-1] != 0:
            path.append(str(l_fathers[x-1]))
            x = l_fathers[x-1]
        path.reverse()
        sys.stdout.write(" ".join(path))
        sys.stdout.write("\n")

main()