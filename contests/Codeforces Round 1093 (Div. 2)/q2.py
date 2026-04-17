import math
import heapq

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=1
    s=True
    for i in range(1,n):
        if a[i] == a[i-1]:
            c+=1
        else:
            c=1
        if c>=m:
            s=False
            break
    print("YES") if s else print("NO")