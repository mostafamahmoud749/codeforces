t=int(input())
for k in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    y=0
    for i in a:
        if i==0:
            x+=1
            if x>y:
                y=x
        else:
            x=0
    print(y)