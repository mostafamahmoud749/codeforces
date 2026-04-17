t=int(input())
xcor=[10000,-10000]
ycor=[10000,-10000]
for _ in range(t):
    x,y=map(int,input().split())
    xcor[0]=min(xcor[0],x)
    xcor[1]=max(xcor[1],x)
    ycor[0]=min(ycor[0],y)
    ycor[1]=max(ycor[1],y)

print(xcor[0],ycor[0])
print(xcor[1],ycor[0])
print(xcor[1],ycor[1])
print(xcor[0],ycor[1])
