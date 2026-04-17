t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=input()
    b=input()
    i=0
    j=0
    res=0
    while i-j<n and i<m:
        if a[i-j]==b[i]:
            i+=1
            res=max(res,i-j)
            c+=1
        else:
            i+=1
            j+=1
    print(res)