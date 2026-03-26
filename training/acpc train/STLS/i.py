import heapq
x,n=map(int,input().split())
a=list(map(int,input().split()))
heapq.heapify(a)
res=0
while len(a)>1:
    e1=heapq.heappop(a)
    e2=heapq.heappop(a)
    s=e1+e2
    res+=s
    heapq.heappush(a,s)


print(res)