t=int(input())
for i in range(t):
    x=input()
    y=[]
    for k in x:
        y.append(k)
    y.pop()
    y.pop()
    y.append("i")
    print(*y,sep="")