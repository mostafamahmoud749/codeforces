import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    db={}
    res=-1
    for i in range(n):
        db[a[i]]=i
    for i in range(n-1,-1,-1):
        if a[i]==1:
            res=(i*2)+2
            break
        else:
            r1=db.get(a[i]+1,-1)
            r2=db.get(a[i]-1,-1)
            if r1!=-1 or r2!=-1:
                res=i+max(r1,r2)+2
                print(r1,r2)
                break
    print(res)



