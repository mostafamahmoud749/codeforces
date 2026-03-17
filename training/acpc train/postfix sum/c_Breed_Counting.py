n,q=map(int,input().split())
prefix={
    1:[0]*(n+1),
    2:[0]*(n+1),
    3:[0]*(n+1)
}

for i in range(1,n+1):
    breed=int(input())
    for j in range(1,4):
        prefix[j][i]=prefix[j][i-1]
    prefix[breed][i]+=1

for i in range(q):
    res=[]
    l,r=map(int,input().split())
    for j in range(1,4):
        res.append(prefix[j][r]-prefix[j][l-1])
    print(*res)