t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    res=0
    for i in range(n):
        res=max(max(map(int,input().split())),res)
    print(res-1)