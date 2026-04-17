import math
import heapq

t=int(input())
for _ in range(t):
    n,m,a,b=map(int,input().split())
    # if math.gcd(n,m)<=2 and math.gcd(m,b)==1 and math.gcd(n,a)==1:
    #     print("YES")
    # else:
    #     print("NO")
    l=[]
    curi=0
    curj=0
    for i in range(n):
        l.append([-1]*m)
    s=1
    while l[curi][curj]==-1:
        l[curi][curj] = 1
        if s%2==0:
            curj=(curj+b)%m
            s+=1
        else:
            curi=(curi+a)%n
            s+=1
    print("YES") if s==(n*m) else print("NO")