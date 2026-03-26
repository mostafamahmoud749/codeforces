import sys
import heapq

input = sys.stdin.buffer.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    bonus=[]
    for i in range(n):
        if a[i]!=0:
            heapq.heappush(bonus, -a[i])
        else:
            if len(bonus)>0:
                res-=heapq.heappop(bonus)
    print(res)