import sys 
sys.setrecursionlimit(2505)

def dfs(i,j):
    visited[i][j]=True
    if a[i][j]=="#":
        return
    if a[i-1][j]!="#" and not visited[i-1][j]:
        dfs(i-1,j)

    if a[i+1][j]!="#" and not visited[i+1][j]:
        dfs(i+1,j)

    if a[i][j-1]!="#" and not visited[i][j-1]:
        dfs(i,j-1)

    if a[i][j+1]!="#" and not visited[i][j+1]:
        dfs(i,j+1)
    




t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=[]

    visited=[[False]*(m+2) for _ in range(n+2)]

    a.append(["#"]*(m+2))
    for i in range(n):
        x=list(input().strip())
        a.append(["#"]+x+["#"])
    a.append(["#"]*(m+2))

    s=True
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j]=="B":
                if a[i+1][j]=="G" or a[i-1][j]=="G" or a[i][j+1]=="G" or a[i][j-1]=="G":
                    s=False
                    break

                if a[i+1][j]!="B":
                    a[i+1][j]="#"

                if a[i-1][j]!="B":
                    a[i-1][j]="#"

                if a[i][j+1]!="B":
                    a[i][j+1]="#"

                if a[i][j-1]!="B":
                    a[i][j-1]="#"
        if not s:
            break
    
    if not s:
        print("NO")
        continue

    dfs(n,m)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j]=="B" and visited[i][j]==True:
                s=False
                break
            if a[i][j]=="G" and visited[i][j]!=True:
                s=False
                break
        if not s:
            break
    
    print("YES") if s else print("NO")


