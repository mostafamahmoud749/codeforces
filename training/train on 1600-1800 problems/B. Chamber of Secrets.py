import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n,m=LII()
a=[]

for _ in range(n):
    a.append(input())

l=[[[float("inf")]*4 for _ in range(m)] for _ in range(n)]
dir=[(1,0,0),(-1,0,1),(0,1,2),(0,-1,3)]

# i,j,d,c

q=deque([(0,0,2)])
l[0][0][2]=0

if a[0][0]=="#":
    l[0][0][0]=1
    q.append((0,0,0))

while q:
    ci,cj,d=q.popleft()
    if a[ci][cj]=="#":
        for u in dir:
            t=u[2]
            if l[ci][cj][d]+1<l[ci][cj][t]:
                l[ci][cj][t]=l[ci][cj][d]+1
                q.append((ci,cj,t))

    ni,nj=ci+dir[d][0],cj+dir[d][1]

    while 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]==".":
        ni+=dir[d][0]
        nj+=dir[d][1]

    if 0<=ni<=n-1 and 0<=nj<=m-1:
        if l[ci][cj][d]<l[ni][nj][d]:
            l[ni][nj][d]=l[ci][cj][d]
            q.appendleft((ni,nj,d))

# print(l[n-1][m-1])

r=-1
for j in range(m-1,-1,-1):
    if a[n-1][j]=="#":
        r = j
        break

res=float("inf")
if r!=-1:
    for j in range(4):
        if j==2:
            res=min(res,l[n-1][r][2])
        else:
            res=min(res,l[n-1][r][j]+1)
print(res) if res!=float("inf") else print(-1)