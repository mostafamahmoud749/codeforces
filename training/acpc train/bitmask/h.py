n,m,k=map(int,input().split())
res=0
a=[]
for _ in range(m+1):
    a.append(int(input()))

for i in range(m):
    if (a[i]^a[-1]).bit_count()<=k: res+=1
print(res)