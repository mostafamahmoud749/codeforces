from collections import deque

n=int(input())
a=set()

adj={}
visited=set()

for i in range(n):
    x,y=map(int,input().split())
    a.add((x,y))

for i,j in a:
    for ci in range(1,1001):
        if  (ci,j) in a:
            if (i,j) in adj:
                adj[(i,j)].append((ci,j))
                
            else:
                adj[(i,j)]=[(ci,j)]

    for cj in range(1,1001):
            if  (i,cj) in a:
                if (i,j) in adj:
                    adj[(i,j)].append((i,cj))
                else:
                    adj[(i,j)]=[(i,cj)]


res=0

for i,j in adj.keys():
    if (i,j) not in visited:
        res+=1
        q=deque([(i,j)])
        visited.add((i,j))

        while q:
            ci,cj=q.popleft()
            for ni,nj in adj[(ci,cj)]:
                if (ni,nj) not in visited:
                    visited.add((ni,nj))
                    q.append((ni,nj))

print(res-1)