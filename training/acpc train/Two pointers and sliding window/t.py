t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    p=[0]*(n+1)
    db={0:1}
    res=0
    for i in range(1,n+1):
        p[i]=p[i-1]+int(a[i-1])
        cur=p[i]-i
        if cur in db:
            res+=db[cur]
            db[cur]+=1
        else:
            db[cur]=1
    print(res)