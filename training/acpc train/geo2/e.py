import math


n,r0=map(int,input().split())
a=[]

for i in range(n):
    r,x,y=map(int,input().split())
    a.append([r,x,y])

res=0

for x in range(-r0,r0+1):
    for y in range(-r0,r0+1):
        s=False
        if x*x+y*y<=r0*r0:
            for r1,x1,y1 in a:
                if (x-x1)**2 + (y-y1)**2 <=r1*r1:
                    s=True
                    break
        if s:
            res+=1

print(res)