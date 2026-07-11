import sys
sys.setrecursionlimit(100005)

def solve(i,j):
    if i==x2 and j==y2:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    
    res=float("inf")
    for k in move:
        cost=0
        newi=i
        newj=j
        for c in k:
            if c=="U" and newi>=1 and a[newi-1][newj]!=1:
                newi-=1
                cost+=1
                # print("u")
            elif c=="R" and newj<=m-2 and a[newi][newj+1]!=1:
                newj+=1
                cost+=1
                # print("r",newi,newj)
            elif c=="D" and newi<=n-2 and a[newi+1][newj]!=1:
                newi+=1
                cost+=1
                # print("d",newi,newj)
            elif c=="L" and newj>=1 and a[newi][newj-1]!=1:
                newj-=1
                cost+=1
                # print("l")
        if visited[newi][newj]==-1 or cost<visited[newi][newj]:
            visited[newi][newj]=cost
            res=min(res,cost+solve(newi,newj))
    
    dp[i][j]=res
    return res

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input().strip()))
print(a)

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())

move=[]
k=int(input())

for i in range(k):
    move.append(list(input().strip()))
print(move)
dp=[[-1]*(m+1) for _ in range(n+1)]
visited=[[-1]*m for _ in range(n)]

res=solve(x1,y1)

print(res) if res!=float("inf") else print(-1)