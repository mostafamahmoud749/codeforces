import math


n=int(input())
a=list(map(int,input().split()))
c25=0
c50=0
s=True
for i in range(n):
    if a[i]==25:
        c25+=1
    elif a[i]==50:
        c25-=1
        c50+=1
        if c25<0:
            s=False
            break
    else:
        if c50>0 and c25>0:
            c50-=1
            c25-=1
        elif c25>2:
            c25-=3
        else:
            s=False
            break
print("YES") if s else print("NO")