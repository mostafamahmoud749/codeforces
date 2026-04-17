n,k,g=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if g-1==i:
        continue
    else:
        s+=a[i]
res=k-s
print(0) if res<=0 else print(res)