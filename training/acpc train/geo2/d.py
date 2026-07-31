import math

v,s=map(int,input().split())


h=s/(2.0*math.sin(math.pi/v))

c=0+0j


r=abs(h-c)
print(f"{math.pi*(r**2):.6f}")

