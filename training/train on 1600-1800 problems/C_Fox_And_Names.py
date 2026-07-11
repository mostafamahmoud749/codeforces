def dfs(v):
    global cyc
    
    visited[v]=2
    for i in per[v]:
        if visited[i]==2:
            cyc=True
        elif visited[i]==0:
            dfs(i)
    visited[v]=1
    path.append(chr(v+97))




n=int(input())
a=[]
for _ in range(n):
    a.append(input())


per=[[] for _ in range(26)]
visited=[0]*(26)
s=True

for i in range(n-1):
    p=True
    for j in range(min(len(a[i]),len(a[i+1]))):
        if a[i][j]!=a[i+1][j]:
                per[ord(a[i][j])-97].append(ord(a[i+1][j])-97)
                p=False
                break
    
    if p and len(a[i+1])<len(a[i]):
        s=False
        break


if not s:
    print("Impossible")
    exit()

path=[]
for i in range(26):
    cyc=False
    if visited[i]==0:
        dfs(i)
    if cyc:
        break

print("".join(path[::-1])) if not cyc else print("Impossible")

