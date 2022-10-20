import sys


def conv(l):
    for i in range(len(l)):
        l[i] = int(l[i])


def rec_insert(x, l):
    n = len(l)
    if n == 0:
        return [x]
    else:
        for i in range(n):
            if x <= l[i]:
                return l[:i] + [x] + l[i:]
        l.append(x)
        return l


def ind_insert(x, l):
    compteur = 0
    for i in range(len(l)):
        if x == l[i]:
            return i


def fusion(l1, l2):
    emp = [0] * len(l2)
    for i in range(len(l2)):
        l1 = rec_insert(l2[i], l1)
        emp[i] = ind_insert(l2[i], l1)
    return emp, l1


def main():
    n, m = input().split()
    n, m = int(n), int(m)
    l1, l2 = input().split(), input().split()
    conv(l1), conv(l2)
    l_emp, l_tot = fusion(l1, l2)
    for i in range(m):
        print(l_emp[i], end=" ")
    print("")
    for i in range(len(l_tot)):
        print(l_tot[i], end=" ")


main()
