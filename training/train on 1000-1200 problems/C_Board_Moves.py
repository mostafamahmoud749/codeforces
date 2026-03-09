t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    pro=0
    for i in range(1,n+1,2):
        res+=pro*((i*4)-4)
        pro+=1
    print(res)