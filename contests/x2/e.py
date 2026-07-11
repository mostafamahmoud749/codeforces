n,m=map(int,input().split())

x1=-1
y1=-1
x2=-1
y2=-1

a=[]
for i in range(n):
    a.append(list(input().strip()))

s=False

for i in range(n):
    if y1==-1:
        for j in range(m):
            if a[i][j]=="+":
                x1=j
                y1=i
                break
    else:
        for j in range(x1+1,m):
            if a[i][j]=="+":
                x2=j
                y2=i
                s=True
                break
    if s:
        break

# print(x2,x1)
# print(y2,y1)
if s:
    print((x2-x1-1)*(y2-y1-1))