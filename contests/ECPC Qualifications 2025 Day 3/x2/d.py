from collections import deque



a=[["."]*12 for _ in range(12)]
l=[[-1]*12 for _ in range(12)]
parent=[[-1]*12 for _ in range(12)]

a[2][2]="*"
a[2][9]="*"
a[9][2]="*"
a[9][9]="*"


a[5][5]="#"
a[5][6]="#"
a[6][5]="#"
a[6][6]="#"

a[8][1]="#"
a[8][2]="#"
a[9][1]="#"

a[8][9]="#"
a[8][10]="#"
a[9][10]="#"

# print(a)

# multi sourse bfs

q=deque([])
a[2][2]="*"
a[2][9]="*"
a[9][2]="*"
a[9][9]="*"
q.append((2,2))
q.append((2,9))
q.append((9,2))
q.append((9,9))

l[2][2]=0
l[2][9]=0
l[9][2]=0
l[9][9]=0

dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    ci,cj=q.popleft()

    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]
        if 0<=ni<=11 and 0<=nj<=11 and a[ni][nj]!="#" and l[ni][nj]==-1:
            l[ni][nj]=l[ci][cj]+1
            if ni>ci:
                parent[ni][nj]=(ci,cj,"U")
            if ni<ci:
                parent[ni][nj]=(ci,cj,"D")
            if nj>cj:
                parent[ni][nj]=(ci,cj,"L")
            if nj<cj:
                parent[ni][nj]=(ci,cj,"R")
            q.append((ni,nj))



# print()
# print(l)




t=int(input())
for _ in range(t):
    i,j=map(int,input().split())
    i-=1
    j-=1
    ci,cj=i,j
    res=[]
    while parent[ci][cj]!=-1:
        ci,cj,m=parent[ci][cj]
        res.append(m)


    print(l[i][j])
    print("".join(res))