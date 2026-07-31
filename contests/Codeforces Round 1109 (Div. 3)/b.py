from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    s=True

    cur=0

    for i in range(n):
        tar=i+1
        if a[i]<tar:
            cur-=tar-a[i]
            if cur<0:
                s=False
                break
        else:
            cur+=a[i]-tar
    print("YES") if s else print("NO")
