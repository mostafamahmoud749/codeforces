import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n,m=LII()
a=[]

ppl=[]
si,sj=-1,-1
ti,tj=-1,-1

for i in range(n):
    x=input()
    for j in range(m):
        if x[j]=="S":
            si,sj=i,j
        elif x[j]=="E":
            ti,tj=i,j
        elif x[j].isdigit() and x[j]!="0":
            ppl.append((i,j,int(x[j])))
    a.append(x)


l=[[-1]*m for _ in range(n)]
q=deque([(ti,tj)])
l[ti][tj]=0

dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    ci,cj=q.popleft()
    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]

        if 0<=ni<=n-1 and 0<=nj<=m-1 and l[ni][nj]==-1 and a[ni][nj]!="T":
            l[ni][nj]=l[ci][cj]+1
            q.append((ni,nj))

res=0
for i,j,c in ppl:
    if l[i][j]!=-1 and l[i][j]<=l[si][sj]:
        res+=c

# print(l)
print(res)
