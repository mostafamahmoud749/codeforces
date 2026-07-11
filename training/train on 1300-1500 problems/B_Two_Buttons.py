from collections import deque

n,m=map(int,input().split())
depth=[-1]*(20005)
visited=[False]*(20005)
visited[n]=True
depth[n]=0
q=deque([n])

while q:
    v=q.popleft()
    if v==m:
        print(depth[v])
        break

    if v-1>0 and not visited[v-1]:
        visited[v-1]=True
        q.append(v-1)
        depth[v-1]=depth[v]+1
    if v*2<20005 and not visited[v*2]:
        visited[v*2]=True
        q.append(v*2)
        depth[v*2]=depth[v]+1

