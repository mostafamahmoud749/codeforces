import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()
for _ in range(t):
    n,m=LII()
    a=[]
    for i in range(n):
        x=list(input().strip())
        for j in range(m):
            if x[j]=="L":
                si,sj=i,j
                
        a.append(x)

    
    dir=[(1,0),(-1,0),(0,1),(0,-1)]


    q=deque([(si,sj)])

    while q:
        ci,cj=q.popleft()

        for u in dir:
            ni=ci+u[0]
            nj=cj+u[1]
            if 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]==".":
                c=0
                for v in dir:
                    vni=ni+v[0]
                    vnj=nj+v[1]

                    if 0<=vni<=n-1 and 0<=vnj<=m-1 and a[vni][vnj]==".":
                        c+=1

                if c<=1:
                    a[ni][nj]="+"
                    q.append((ni,nj))

    for i in a:
        print("".join(i))