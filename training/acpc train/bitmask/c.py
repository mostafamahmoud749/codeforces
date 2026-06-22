t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in a:
        res|=i
    print(res)