n=int(input())
a=list(map(int,input().split()))
p=[0]*(n+1)
db={0: 1}
s=False
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
    if p[i]%n in db:
        s=True
        break
    else:
        db[p[i]%n]=1
print("YES") if s else print("NO")