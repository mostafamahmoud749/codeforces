import sys
from collections import deque
import array

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
input = sys.stdin.readline

n,m=list(map(int,input().split()))
k=int(input())
a=list(map(int,input().split()))

l = [array.array('h', [-1]) * m for _ in range(n)]


q=deque([])
for i in range(k):
    q.append([a[2*i]-1,a[2*i+1]-1])
    l[a[2*i]-1][a[2*i+1]-1]=0

# print(q)

dir=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
    ]

li,lj=0,0
while q:
    i,j=q.popleft()
    li=i
    lj=j
    for x,y in dir:
        ni=i+x
        nj=j+y
        if 0<=ni<=n-1 and 0<=nj<=m-1 and l[ni][nj]==-1:
            l[ni][nj]=l[i][j]+1
            q.append([ni,nj])

# print(l)

print(li+1,lj+1)

