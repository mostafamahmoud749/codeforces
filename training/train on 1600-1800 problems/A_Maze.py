import sys
sys.setrecursionlimit((500*500)+5)

def dfs(i,j):
    visited[i][j]=True

    if len(valid)==(n*m)-notvalid:
        return

    valid.append([i,j])
    
    if a[i-1][j]==a[i][j] and not visited[i-1][j]:
        dfs(i-1,j)

    if a[i+1][j]==a[i][j] and not visited[i+1][j]:
        dfs(i+1,j)

    if a[i][j-1]==a[i][j] and not visited[i][j-1]:
        dfs(i,j-1)

    if a[i][j+1]==a[i][j] and not visited[i][j+1]:
        dfs(i,j+1)
    



n,m,k=map(int,input().split())
a=[]

# padd with walls
a.append(["#"]*(m+2))
for i in range(n):
    x=list(input().strip())
    a.append(["#"]+x+["#"])
a.append(["#"]*(m+2))

# print(a)

per=[]
visited=[[False]*(m+2) for _ in range(n+2)]
notvalid=k
indx=-1

for i in range(1,n+1):
    for j in range(1,m+1):
        if indx==-1 and a[i][j]==".":
            indx=[i,j]

        if a[i][j]=="#":
            notvalid+=1

valid=[]


dfs(indx[0],indx[1])

# print(valid)

# print((n*m)-notvalid)

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==".":
            a[i][j]="X"

for i in valid:
    a[i[0]][i[1]]="."


for i in range(1,n+1):
    print("".join(a[i][1:m+1]))
