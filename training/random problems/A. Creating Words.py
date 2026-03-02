n=int(input())
for i in range(n):
    n,m=map(str,input().split())
    y=[m[0]]
    x=[n[0]]
    for k in range(1,3):
        y.append(n[k])
        x.append(m[k])
    print(*y," ",*x ,sep="")