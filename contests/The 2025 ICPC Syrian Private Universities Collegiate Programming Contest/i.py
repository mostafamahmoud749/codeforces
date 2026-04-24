import math

n,x=map(int,input().split())
a=list(map(int,input().split()))
db={}
res=0
for i in range(n):
    if (-a[i])%x in db:
        for j in db[(-a[i])%x]:
            if (a[i]*a[j])%x==0:
                res+=1
    rem=a[i]%x
    if rem in db:
        db[rem].append(i)
    else:
        db[rem]=[i]
print(res)