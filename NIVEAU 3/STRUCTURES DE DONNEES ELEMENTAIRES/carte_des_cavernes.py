def main():
    n = int(input())
    i = 0
    l = input()
    compteur = 0
    while i < n:
        if l[i] == ' ':
            i += 1
        elif l[i] =='(':
            compteur += 1
            i+=1
        else:
            compteur -=1
            i+=1
        if compteur < 0:
            print("0")
            break
    if compteur > 0 :
        print("0")
    else : 
        print("1")

main()