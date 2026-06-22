import math
t=int(input())
for _ in range(t):
    a,b,x=map(int,input().split())
    res=abs(a-b)

    la=[]
    i=0
    while a!=0:
        la.append([a,i])
        a//=x
        i+=1
    la.append([0,i])

    lb=[]
    i=0
    while b!=0:
        lb.append([b,i])
        b//=x
        i+=1
    lb.append([0,i])
    
    for i in la:
        for j in lb:
            res=min(res,i[1]+j[1]+abs(i[0]-j[0]))
    print(res)