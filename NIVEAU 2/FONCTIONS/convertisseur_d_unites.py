def fahrenheit(n):
    f = 32 + 1.8 * n
    print(str(f) + " f")


def livre(n):
    l = 0.002205 * n
    print(str(l) + " l")


def pied(n):
    p = 3.2808 * n
    print(str(p) + " p")


nbval = int(input())
for i in range(nbval):
    val = input().split(" ")
    if val[1] == "c":
        fahrenheit(float(val[0]))
    if val[1] == "g":
        livre(float(val[0]))
    if val[1] == "m":
        pied(float(val[0]))
