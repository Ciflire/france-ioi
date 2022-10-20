alphabet = str(input())


def decrypte(a, car):
    return a[ord(car) % 97]


decrypter = str(input())


def main(m):
    n = len(m)
    mot = ""
    for i in range(n):
        if m[i].isalpha():
            if m[i].isupper():
                mot += decrypte(alphabet, m[i].lower()).upper()
            else:
                mot += decrypte(alphabet, m[i])
        else:
            mot = mot + m[i]
    return mot


print(main(decrypter))
