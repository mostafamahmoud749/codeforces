import heapq

n,k=map(int,input().split())
a=list(map(int,input().split()))
h=[]
res=0
cres=0
for i in range(k):
    cres+=a[i]
    heapq.heappush(h,(a[i],i))
res=cres-h[0][0]
for i in range(k,n):
    cres+=a[i]-a[i-k]
    heapq.heappush(h,(a[i],i))
    while h[0][1]<=i-k:
        heapq.heappop(h)
    res=max(res,cres-h[0][0])
print(res)
