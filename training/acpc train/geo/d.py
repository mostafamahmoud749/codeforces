import sys
import math

sys.stdin = open('area1.in', 'r')
sys.stdout = open('area1.out', 'w')

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def areaTriangle(a,b,c):
    return abs(cross(b-a,c-a))/2

x1,y1,x2,y2,x3,y3=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j
p3=x3+y3*1j

print(areaTriangle(p1,p2,p3))
