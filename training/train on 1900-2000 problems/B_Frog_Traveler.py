import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
a=[0]+list(map(int,input().split()))
b=[0]+list(map(int,input().split()))

parent=[-1]*(n+1)
prev=[-1]*(n+1)
l=[-1]*(n+1)
l[n]=0

d=list(range(n+2))

def find(x):
    while d[x]!=x:
        d[x]=d[d[x]]
        x=d[x]
    return x

q=deque([n])



while q:
    v=q.popleft()
    
    jumps=a[v]

    if l[0]!=-1:
        break

    cur=v-jumps
    if cur<0:
        cur=0

    i=find(cur)
    while i<=v-1:
        slip=b[i]
        to=i+slip
        if l[to]==-1:
            l[to]=l[v]+1
            q.append(to)
            parent[to]=i
            prev[to]=v

        d[i]=find(i+1)
        i=find(i)

res=[]
print(l[0])
cur=0

# print(parent)

if l[0]!=-1:
    while parent[cur]!=-1:
        res.append(parent[cur])
        cur=prev[cur]
    print(*res[::-1])