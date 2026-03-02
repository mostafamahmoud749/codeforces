n=int(input())
x=0
y=0
xg=0
yg=0
for i in range(n):
    m=input()
    if x==0:
        x=m
    elif y==0 and m!=x:
        y=m
    if x==m:
        xg+=1
    else:
        yg+=1
if xg>yg:
    print(x)
else:
    print(y)



