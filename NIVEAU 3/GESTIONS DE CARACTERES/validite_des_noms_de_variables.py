nbvar = int(input())


def est_correct(var):
    n = len(var)
    if not(var[0].isalpha()) and not(var[0] == "_"):
        print("NO")
        return None
    for i in range(1, n):
        if not(var[i].isalpha()) and not(var[i] == "_") and not(var[i].isdigit()):
            print("NO")
            return None
    print("YES")


def resolution(nbvar):
    for i in range(nbvar):
        var = str(input())
        est_correct(var)


resolution(nbvar)
