from collections import deque

n=int(input())
c=list(map(int,input().split()))
a=list(map(int,input().split()))


degree=[0] * (n+1)

for i in range(n):
  degree[a[i]]+=1

q=deque([])

for i in range(1,n+1):
  if degree[i]==0:
    q.append(i)

removed=[False] * (n+1)

while q:
  v=q.popleft()
  removed[v]=True

  u=a[v-1]
  degree[u]-=1
  if degree[u]==0:
    q.append(u)

res=0

for i in range(1,n+1):
  if not removed[i]:
    mn=c[i-1]
    v=i
    while not removed[v]:
      removed[v]=True
      if c[v-1]<mn:
        mn=c[v-1]
      v=a[v-1]

    res+=mn

print(res)

