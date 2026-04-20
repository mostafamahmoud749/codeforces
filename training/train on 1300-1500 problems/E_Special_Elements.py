t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for k in range(n):
        i=0
        j=0
        c=0
        while i<n :
            c+=a[i]
            while c>a[k]:
                c-=a[j]
                j+=1
            i+=1
            if c==a[k] and i-j>1:
                res+=1
                break
    print(res)
