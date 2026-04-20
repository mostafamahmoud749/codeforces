n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
c=0
res=0
w=0
for o in range(n):
    if b[o]==1:
        w+=a[o]
while i<k:
    if b[i]==0:
        c+=a[i]
    i+=1
    res=max(res,c)
while i<n:
    if b[i]==0:
        c+=a[i]
    if b[j]==0:
        c-=a[j]
    i+=1
    j+=1
    res=max(res,c)
print(res+w)
