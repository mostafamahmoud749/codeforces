def solve(indx,d):
    if indx==n:
        if d==0:
            return 0
        return -float("inf")
    if db[indx][d]!=-1:
        return db[indx][d]
    ch1=0
    ch2=0
    ch1=a[indx]+solve(indx+1,d+a[indx]-(b[indx]*k))
    ch2=solve(indx+1,d)
    res=max(ch1,ch2)
    db[indx][d]=res
    return res

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
db=[[-1]* 100000 for _ in range(n)]
res=solve(0,0)
print(res) if res!=0 else print(-1)