t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    a=list(map(int,input().split()))
    i,j=0,0
    c=0
    res=0
    while i<n:
        c+=a[i]
        while c>w:
            c-=a[j]
            j+=1
        res=max(res,c)
        if res==w:
            break
        i+=1
    print(res)