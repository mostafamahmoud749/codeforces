
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    res=0
    for i in a:
        res+=min(i%k,k-(i%k))
    print(res)