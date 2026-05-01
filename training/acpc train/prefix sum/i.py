n=int(input())
a=list(map(int,input().split()))
db={0:1}
p=[0]*(n+1)
res=0
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
    rem=p[i]%n
    if rem in db:
        res+=db[rem]
        db[rem]+=1
    else:
        db[rem]=1
print(res)