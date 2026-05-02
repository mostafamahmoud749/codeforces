n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
res=0
while i<=n-1:
    if j<=m-2 and abs(a[i]-b[j])>=abs(a[i]-b[j+1]):
        j+=1
    else:
        res=max(res,abs(a[i]-b[j]))
        i+=1
print(res)