n = int(input())

def bubble_sort(l1,l2):
    for i in range(n-1):
        for j in range(n-i-1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                l2[j], l2[j+1] = l2[j+1], l2[j]
            elif l1[j] == l1[j+1]:
                if l2[j] > l2[j+1]:
                    l2[j+1] , l2[j] = l2[j] , l2[j+1]
    return l1,l2

def main():
    l1,l2 = [],[]
    for i in range (n):
        x , y = input().split()
        x , y = int(x), int(y)
        l2.append(x)
        l1.append(y)
    l_pol , l_id = bubble_sort(l1,l2)
    for i in range(n):
        print(l_pol[i] ,l_id[i])

main()