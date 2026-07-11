

t=int(input())
for _ in range(t):
    n=int(input())

    adj=[set() for _ in range(n+1)]

    deg=[]
    for i in range(0,n+1):
        deg.append([0,i])

    for i in range(n-1):
        x,y=map(int,input().split())
        adj[x].add(y)
        adj[y].add(x)
        deg[x][0]+=1
        deg[y][0]+=1
    
    deg.sort(reverse=True)

    res=0

    for i in range(n):
        c1,v=deg[i]
        for j in range(i+1,n):
            c2,u=deg[j]
            if c1+c2-1<=res:
                break
            if u in adj[v]:
                c2-=1
            
            res=c1+c2-1
        

    print(res)

    