from collections import deque

n,x=map(int,input().split())



visited={x}
res=-1


q=deque([[x,0]])
while q:
    x,d=q.popleft()
    if len(str(x))==n:
        res=d
        break

    st=set(int(d) for d in str(x) if d>"1")
    

    for i in st:
        if (x*i) not in visited and len(str(x*i))<=n:
            q.append([x*i,d+1])
            visited.add(x*i)

print(res)