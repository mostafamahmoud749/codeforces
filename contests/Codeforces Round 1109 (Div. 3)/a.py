from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(input().strip())

    res=0
    curr=0
    for i in a:
        if i=="#":
            curr+=1
        if i=="*" and curr!=0:
            res=max(res,math.ceil(curr/2))
            curr=0
    
    res=max(res,math.ceil(curr/2))
    print(res)