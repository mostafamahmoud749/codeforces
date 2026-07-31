from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    else:
        res=[1,2,3]
        curs=6
        while len(res)<n:
            res.append(curs)
            curs*=2
        
        print(*res)