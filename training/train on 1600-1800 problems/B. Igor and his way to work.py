from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))


n,m=LII()
a=[]
si,sj=-1,-1
ti,tj=-1,-1
for i in range(n):
    x=input()
    for j in range(m):
        if x[j]=="S":
            si,sj=i,j
        elif x[j]=="T":
            ti,tj=i,j
    a.append(x)




l=[[float("inf")]*m for _ in range(n)]
l[si][sj]=0
q=deque([(si,sj,-1)])

dir=[(1,0,0),(-1,0,1),(0,1,2),(0,-1,3)]

while q:
    ci,cj,t=q.popleft()
    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]

        cost=0 if t==-1 or t==u[2] else 1

        if 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]!="*":
            if l[ni][nj]>l[ci][cj]+cost:
                l[ni][nj]=l[ci][cj]+cost
                if cost==0:
                    q.appendleft((ni,nj,u[2]))
                else:
                    q.append((ni,nj,u[2]))


print("YES") if l[ti][tj]<=2 else print("NO")