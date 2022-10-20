bonessai = 0
boncode = 4242
while bonessai != 2:
    essai = int(input())
    print("Entrez le code :")
    if essai == boncode and bonessai < 1:
        print("Encore une fois.")
        bonessai += 1
    elif essai == boncode and bonessai == 1:
        print("Bravo.")
        bonessai += 1
