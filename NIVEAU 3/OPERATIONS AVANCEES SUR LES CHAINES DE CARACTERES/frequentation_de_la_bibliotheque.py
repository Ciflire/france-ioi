def somme_liste(l):
    if l == []:
        return 0
    else:
        return int(l[0]) + somme_liste(l[1:])


def main():
    res = 0
    for i in range(100):
        try:
            line = str(input())
            liste = line.split()
            res += somme_liste(liste)
        except:
            print(res)
            return None


main()
