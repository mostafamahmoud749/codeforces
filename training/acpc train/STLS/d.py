import heapq

n=int(input())
a=list(map(int,input().split()))

res=0
cur_hel=0
neg=[]

for i in range(n):
    cur_hel+=a[i]
    res+=1
    if a[i]<0:
        heapq.heappush(neg,a[i])
    if cur_hel<0:
        cur_hel-=heapq.heappop(neg)
        res-=1

print(res)