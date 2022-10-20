import sys

def main():
    l1 = sys.stdin.readline()
    t1 = list(map(int,sys.stdin.readline().split()))
    l2 = sys.stdin.readline()
    t2 = list(map(int,sys.stdin.readline().split()))
    i1,i2=0,0
    t=[]
    while i1<l1 and i2<l2:
        if t1[i1]<t2[i2]:
            t.append(t1[i1])
            i1+=1
        else:
            t.append(t2[i2])
            i2+=1
    if i1==l1:
        t=t+t2[i2:]
    else:
        t=t+t1[i1:]
    t = list(map(str,t))
    sys.stdout.write(" ".join(t))