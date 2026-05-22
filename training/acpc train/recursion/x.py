def genrate(s,indx,c):
    if indx==n:
        if c%k==0:
            print(*s)
        return
    for i in range(1,a[indx]+1):
        genrate(s+[i],indx+1,c+i)

n,k=map(int,input().split())
a=list(map(int,input().split()))
genrate([],0,0)