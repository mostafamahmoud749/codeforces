n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
s=set()
p=n-1
for i in range(n-1,-1,-1):
    while b[p] in s and p>=0:
        p-=1
    if a[i]==b[p]:
        p-=1
        continue
    else:
        s.add(a[i])
        res+=1
print(res)