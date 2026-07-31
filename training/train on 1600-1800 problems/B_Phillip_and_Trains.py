from collections import deque

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())

    a=list()
    for i in range(3):
        a.append(list(input().strip()))

    si=0
    sj=0

    if a[1][0]=="s":
        si=1
    elif a[2][0]=="s":
        si=2

    visited=[]
    for i in range(3):
        cur=[False]*n
        for j in range(n):
            if a[i][j]!="." and a[i][j]!="s":
                cur[j]=True
        visited.append(cur)


    q=deque([[si,sj]])
    found=False

    while q:
        i,j=q.popleft()

        if j+1>=n-1:
            found=True
            break

        if not visited[i][j+1]:

            # if we stay idel after moving right 
            if (not visited[i][j+2]) and (j+3>n-1 or not visited[i][j+3]):
                if j+3>=n-1:
                    found=True
                    break
                if not visited[i][j+3]:
                    q.append([i,j+3])
                    visited[i][j+3]=True

            # if we go up
            if i>0 and (not visited[i-1][j+1]) and ((not visited[i-1][j+2]) and (j+3>n-1 or not visited[i-1][j+3])):
                if j+3>=n-1:
                    found=True
                    break
                if not visited[i-1][j+3]:
                    q.append([i-1,j+3])
                    visited[i-1][j+3]=True

            # if we go down
            if i<2 and (not visited[i+1][j+1]) and (not visited[i+1][j+2]) and (j+3>n-1 or not visited[i+1][j+3]):
                if j+3>=n-1:
                    found=True
                    break
                if not visited[i+1][j+3]:
                    q.append([i+1,j+3])
                    visited[i+1][j+3]=True

    print("YES") if found else print("NO")