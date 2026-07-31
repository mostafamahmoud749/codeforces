from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    s=True

    g=math.gcd(x,y)

    for i in range(n):
        if a[i]%g!=(i+1)%g:
            s=False
            break

    print("YES") if s else print("NO")