n,m=map(int,input().split())
s=int(input())
db=[]
for i in range(n):
    db.append([])
    for j in range(m):
        db[i].append([0,False])
for i in range(s):    
    d=input().split()
    c,p=int(d[0]),int(d[1])
    v=d[2]
    if v!="AC":
        db[c-1][p-1][0]+=1
    else:
        db[c-1][p-1][1]=True
q=int(input())
p=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if db[i-1][j-1][1]==True:
            p[i][j]=p[i][j-1]+p[i-1][j]-p[i-1][j-1]+db[i-1][j-1][0]
        else:
            p[i][j]=p[i][j-1]+p[i-1][j]-p[i-1][j-1]
for _ in range(q):
    c1,p1,c2,p2=map(int,input().split())
    res = p[c2][p2]-p[c1-1][p2]-p[c2][p1-1]+p[c1-1][p1-1]
    print(res)