import sys

n = int(sys.stdin.readline())
tableau = [[' '] * n for _ in range (n)]

def rec_print(x,y,n,tab):
    if n == 1:
        tab[x][y] = '#' 
    else:
        rec_print(x,y,n//2,tab)
        rec_print(x+n//2,y,n//2,tab)
        rec_print(x,y+n//2,n//2,tab)
        return tab

def main():
    rec_print(0,0,n,tableau)
    for x in tableau:
       sys.stdout.write("".join(x)+"\n")
       

main()