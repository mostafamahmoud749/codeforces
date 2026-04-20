t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    j=0
    c=0
    res=-1
    for i in range(n):
        c+=a[i]
        while c>s and j<=i:
            c-=a[j]
            j+=1
        if c==s:
            res=max(res,i-j+1)
    if res==-1:
        print(-1)
    else:
        print(n-res)