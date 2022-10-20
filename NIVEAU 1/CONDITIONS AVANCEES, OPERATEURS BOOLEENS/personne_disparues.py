pcherchee = int(input())
tailleliste = int(input())
var = 0
for i in range(tailleliste):
    preg = int(input())
    if pcherchee == preg:
        var += 1
if var > 0:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")
