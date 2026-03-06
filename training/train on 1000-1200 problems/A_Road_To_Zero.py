t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    res=0

    if (x>0 and y>0) or (x<0 and y<0):
        x=abs(x)
        y=abs(y)
        if a<(b/2):
            print((a*x)+(a*y))
        else:
            print((min(x,y)*b)+((max(x,y)-min(x,y))*a))
    else:
        x=abs(x)
        y=abs(y)
        print((x*a)+(y*a))