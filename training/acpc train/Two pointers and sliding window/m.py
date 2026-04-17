n,k=map(int,input().split())
a=list(map(int,input().split()))
res=0
i=0
j=0
c=0
sindx=0
eindx=0
while i<n:
    if a[i]==1:
        c+=1
        i+=1
    elif a[i]==0 and k>0:
        c+=1
        k-=1
        i+=1
    else:
        if a[j]==1:
            c-=1
            j+=1
        else:
            c-=1
            j+=1
            k+=1
    if c>res:
        sindx=j
        eindx=i
        res=c
for i in range(sindx,eindx):
    a[i]=1
print(res)
print(*a)