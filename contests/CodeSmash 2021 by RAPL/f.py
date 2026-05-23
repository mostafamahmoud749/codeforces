t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    db={}
    for i in a:
        db[i]=db.get(i,0)+1
    res=len(db)
    for i in range(m):
        p,r=map(int,input().split())
        db[a[p-1]]-=1
        if db[a[p-1]]==0:
            res-=1
        a[p-1]+=r
        if db.get(a[p-1],0)==0:
            res+=1
            db[a[p-1]]=1
        else:
            db[a[p-1]]+=1
        print(res)

