import heapq
n=int(input())
a=list(map(int,input().split()))
res=0
b=[]
h=0
for i in range(n):
    h+=a[i]
    res+=1
    if a[i]<0:
        heapq.heappush(b,a[i])
    if h<0:
        h-=heapq.heappop(b)
        res-=1
print(res)