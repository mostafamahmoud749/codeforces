import math
import heapq

t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    b=2*(p+(2*q))+1
    m=int(math.sqrt(b))
    s=False
    for r in range(1,m+1):
        for c in range(1,m+1):
            if ((2*r)+1)*((2*c)+1)==b:
                print(r,c)
                s=True
                break
        if s:
            break
    if s==False:
        print(-1)


