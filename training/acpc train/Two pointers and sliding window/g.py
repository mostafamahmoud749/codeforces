n,t=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=0
s=0
while i<n and t>=a[i]:
    t-=a[i]
    i+=1
    s+=1
res=s
while i<n:
    if a[i]>t:
        t+=a[j]
        j+=1
        s-=1
    else:
        s+=1
        t-=a[i]
        i+=1
    res=max(res,s)
print(res)