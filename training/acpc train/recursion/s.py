def solve(c,indx):
    global res
    if c>=res:
        return
    d=0
    for i in range(m):
        if skills[i]>=x:
            d+=1
    if d==m:
        res=min(res,c)
        return
    if indx==n:
        return
    solve(c,indx+1)
    for j in range(1,len(books[indx])):
        skills[j-1]+=books[indx][j]
    solve(c+books[indx][0],indx+1)
    for j in range(1,len(books[indx])):
        skills[j-1]-=books[indx][j]


n,m,x=map(int,input().split())
books=[]
for i in range(n):
    books.append(list(map(int,input().split())))
res=float("inf")
skills=[0]*m
solve(0,0)
print(res) if res!=float("inf") else print(-1)