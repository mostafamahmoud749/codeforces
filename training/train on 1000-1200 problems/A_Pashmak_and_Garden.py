x1,y1,x2,y2=map(int,input().split())
if x1==x2 and y1==y2:
    print(-1)
elif x1==x2:
    side=abs(y2-y1)
    print(x1+side,y1,x1+side,y2)
elif y1==y2:
    side=abs(x2-x1)
    print(x1,y1+side,x2,y1+side)
else:
    if abs(x2-x1)!=abs(y2-y1):
        print(-1)
    else:
        print(x1,y2,x2,y1)