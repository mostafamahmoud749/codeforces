t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    r=[0]*n
    b=[0]*1001
    p=[0]*(1001)
    for i in range(1001):
        b[i]=[0]*1001
        p[i]=[0]*1001
    for i in range(n):
        mh,mw=map(int,input().split())
        b[mh][mw]+=mh*mw
    for i in range(1,1001):
        for j in range(1, 1001):
            p[i][j]=p[i-1][j]+p[i][j-1]-p[i-1][j-1]+b[i][j]
    for i in range(q):
        sh,sw,bh,bw=map(int,input().split())
        print(p[bh-1][bw-1]-p[sh][bw-1]-p[bh-1][sw]+p[sh][sw])
