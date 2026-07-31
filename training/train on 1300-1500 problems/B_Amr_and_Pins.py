import math

r,x1,y1,x2,y2=map(int,input().split())

p1=x1+y1*1j

p2=x2+y2*1j

print(math.ceil(abs(p1-p2)/(r*2)))