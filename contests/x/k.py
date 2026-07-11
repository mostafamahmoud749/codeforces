t=int(input())
for _ in range(t):
    x1,x2,y1,y2=map(int,input().split())
    res=0
    if y1>=x1:
        res=min(x2,y2)-y1
    if x1>y1:
        res=min(x2,y2)-x1

    print(res) if res>0 else print(0)
