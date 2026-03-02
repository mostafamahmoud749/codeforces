t=int(input())
for i in range(t):
    y=input()
    x=list(map(int,input().split()))
    res=1
    x[x.index(min(x))]+=1
    for k in x:
        res=res*k
    print(res)