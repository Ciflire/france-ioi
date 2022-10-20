debut1 = int(input())
fin1 = int(input())
debut2 = int(input())
fin2 = int(input())
if (debut1 >= debut2) and (fin1 <= fin2):  # cas 1
    print("Amis")
elif (debut1 <= debut2) and (fin1 >= debut2):  # cas 2
    print("Amis")
elif (debut1 <= debut2) and (fin1 >= fin2):  # cas 3
    print("Amis")
elif (debut1 >= debut2) and (debut1 <= fin2):  # cas 4
    print("Amis")
else:
    print("Pas amis")
