n=int(input())
a=list(map(int,input().split()))
m=min(a)
l=n//m
res=[]
for i in range(1,l+1):
    for j in range(9,0,-1):
        if len(res)<i and n-a[j-1]-(m*(l-i))>=0:
            res.append(str(j))
            n-=a[j-1]
print("".join(res)) if res!=[] else print(-1)