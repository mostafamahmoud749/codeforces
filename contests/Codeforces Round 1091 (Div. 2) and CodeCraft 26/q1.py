import math
import heapq

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n*k%2==0 or sum(a)%2!=0:
        print("YES")
    else:
        print("NO")
