import sys
import math

# sys.stdin = open('area.in', 'r')
# sys.stdout = open('area.out', 'w')

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def areaPolygon(p):
    area=0.0
    for i in range(len(p)):
        area+=cross(p[i] , p[(i+1)%len(p)])
    
    return abs(area)/2

n=int(input())
p=[]

for _ in range(n):
    x,y=map(int,input().split())
    p.append(x+y*1j)

print(areaPolygon(p))
