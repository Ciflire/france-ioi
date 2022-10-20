age = int(input())
bagages = int(input())
res = 0
if age < 10:
    res = res + 5
if age >= 10 and age != 60:
    res = res + 30
if age == 60:
    res = res
if bagages >= 20 and age >= 10 and age != 60:
    res = res + 10
print(res)
