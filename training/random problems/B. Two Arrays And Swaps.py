t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=0
    for i in range(k):
        if min(a)>=max(b):
            break
        a[a.index(min(a))],b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
    for i in a:
        res+=i
    print(res)