import sys
sys.setrecursionlimit(1000000)

def dfs(r, c):
    global cres
    visted[r][c] = 1
    cres+=ver[r][c]
    for dr,dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<n and 0<=nc<m and ver[nr][nc]>0 and visted[nr][nc]==0:
            dfs(nr,nc)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ver=[0]*n
    visted=[[0]*m for _ in range(n)]
    res=0
    for i in range(n):
        ver[i]=list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            if visted[i][j]==0 and ver[i][j] > 0:
                cres=0
                dfs(i, j)
                res=max(res,cres)
    print(res)
