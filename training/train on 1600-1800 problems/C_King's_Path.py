from collections import deque

x0,y0,x1,y1=map(int,input().split())

q=int(input())

s=set()

for _ in range(q):
    r,a,b=map(int,input().split())
    for i in range(a,b+1):
        s.add((r,i))

l={(x0,y0):0}

q=deque([(x0,y0)])

while q:
    v=q.popleft()
    x=v[0]
    y=v[1]
    if x==x1 and y==y1:
        break

    if  (x+1,y+1) in s and (x+1,y+1) not in l:
        q.append((x+1,y+1))
        l[(x+1,y+1)]=l[(x,y)]+1

    if  (x+1,y) in s and (x+1,y) not in l:
        q.append((x+1,y))
        l[(x+1,y)]=l[(x,y)]+1

    if  (x,y+1) in s and (x,y+1) not in l:
        q.append((x,y+1))
        l[(x,y+1)]=l[(x,y)]+1

    if  (x+1,y-1) in s and (x+1,y-1)  not in l:
        q.append((x+1,y-1))
        l[(x+1,y-1)]=l[(x,y)]+1

    if  (x-1,y+1) in s and (x-1,y+1) not in l:
        q.append((x-1,y+1))
        l[(x-1,y+1)]=l[(x,y)]+1

    if  (x-1,y-1) in s and (x-1,y-1) not in l:
        q.append((x-1,y-1))
        l[(x-1,y-1)]=l[(x,y)]+1

    if  (x-1,y) in s and (x-1,y) not in l:
        q.append((x-1,y))
        l[(x-1,y)]=l[(x,y)]+1

    if  (x,y-1) in s and (x,y-1)  not in l:
        q.append((x,y-1))
        l[(x,y-1)]=l[(x,y)]+1

print(l.get((x1,y1),-1))


# minx=min(x0,x1)
# maxx=max(x0,x1)
# miny=min(y0,y1)
# maxy=max(y0,y1)

# q=int(input())
# s=[]
# for i in range(q):
#     r,a,b=map(int,input().split())
#     minx=min(minx,r)
#     maxx=max(maxx,r)
#     miny=min(miny,a)
#     maxy=max(maxy,b)
#     s.append([r,a,b])

# a=[["x"] * (maxy-miny+1) for _ in range(maxx-minx+1)]

# l=[[-1] * (maxy-miny+1) for _ in range(maxx-minx+1)]

# for i in s:
#     curr=i[0]-minx
#     for j in range(i[1]-miny,i[2]-miny+1):
#         a[curr][j]="."

# a[x0-minx][y0-miny]="."
# a[x1-minx][y1-miny]="T"

# q=deque([[x0-minx,y0-miny]])
# l[x0-minx][y0-miny]=0

# while q:
#     v=q.popleft()
#     x=v[0]
#     y=v[1]
#     if a[x][y]=="T":
#         break
#     # r
#     if y<maxy-miny and a[x][y+1]!="x" and l[x][y+1]==-1:
#         q.append([x,y+1])
#         l[x][y+1]=l[x][y]+1
#     # rt
#     if  y<maxy-miny and x>0 and a[x-1][y+1]!="x" and l[x-1][y+1]==-1:
#         q.append([x-1,y+1])
#         l[x-1][y+1]=l[x][y]+1
#     # rb
#     if  y<maxy-miny and x<maxx-minx and a[x+1][y+1]!="x" and l[x+1][y+1]==-1:
#         q.append([x+1,y+1])
#         l[x+1][y+1]=l[x][y]+1
#     # t
#     if x>0 and a[x-1][y]!="x" and l[x-1][y]==-1:
#         q.append([x-1,y])
#         l[x-1][y]=l[x][y]+1
#     # tl
#     if y>0 and x>0 and a[x-1][y-1]!="x" and l[x-1][y-1]==-1:
#         q.append([x-1,y-1])
#         l[x-1][y-1]=l[x][y]+1
#     # l
#     if y>0 and a[x][y-1]!="x" and l[x][y-1]==-1:
#         q.append([x,y-1])
#         l[x][y-1]=l[x][y]+1
#     # lb
#     if y>0 and x<maxx-minx and a[x+1][y-1]!="x" and l[x+1][y-1]==-1:
#         q.append([x+1,y-1])
#         l[x+1][y-1]=l[x][y]+1
#     # b
#     if x<maxx-minx and a[x+1][y]!="x" and l[x+1][y]==-1:
#         q.append([x+1,y])
#         l[x+1][y]=l[x][y]+1

# print(l[x1-minx][y1-miny])
