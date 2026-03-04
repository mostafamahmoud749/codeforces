n,x=map(int,input().split())
res=0
for i in range(1,n+1):
    if x<i:
        break
    maxn=i*n
    if x<=maxn and x%i==0:
        res+=1
print(res)