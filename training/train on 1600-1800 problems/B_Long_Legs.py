t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    res=x+y
    for i in range(1,100001):
        res=min(res,(i-1)+((x+i-1)//i)+((y+i-1)//i))
    print(res)