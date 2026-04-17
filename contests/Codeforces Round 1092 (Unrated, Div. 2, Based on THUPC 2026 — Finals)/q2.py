import math
import heapq

t=int(input())
for _ in range(t):
    t,h,u=map(int,input().split())
    res=0
    m=min(t,u)
    res+=m*4
    u-=m
    t-=m
    res+=u*3
    if t==0:
        res+=h*3
    elif h>=(t+1)//2:
        res+=2*t+3*h
    else:
        res+=2*t+3*h+1
    print(res)