n=int(input())
a=list(map(int,input().split()))
p=[0]*n
for i in range(1,n):
    if a[i]>a[i-1]:
        p[i]=p[i-1]+1
    else:
        p[i]=0

res=max(p)+1
for i in range(1,n):
    if p[i]==0:
        k=i+1
        while k<n and p[k]>0:
            k+=1
        if i>=2 and a[i-2]<a[i]:
            res=max(res,p[i-2]+1+(k-i))
        if i<n-1 and a[i-1]<a[i+1]:
            res=max(res,p[i-1]+1+(k-i-1))
print(res)