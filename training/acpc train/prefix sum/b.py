n,x=map(int,input().split())
a=list(map(int,input().split()))
db={}
p=[0]*(n+1)
res=0

for i in range(0,n+1):
    p[i]=a[i-1]+p[i-1]
    if p[i]-x in db:
        res+=db[p[i]-x]
    if p[i] in db:
        db[p[i]]+=1
    else:
        db[p[i]]=1

print(res)