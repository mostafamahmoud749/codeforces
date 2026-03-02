n,m=map(int,input().split())
x=[]
for i in range(n):
    y=input()
    x.append(y)
width=0
hight=0
for k in x:
    count=0
    if "#" in k:
        hight+=1
    for j in k:
        if j=="#":
            count+=1
    if count>width:
        width=count
print((hight+width)*2)