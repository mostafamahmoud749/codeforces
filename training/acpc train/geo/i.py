import sys
import math

sys.stdin = open('distance4.in', 'r')
sys.stdout = open('distance4.out', 'w')

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def dist_pt_segment(seg, p):
    a, b = seg
    # If the angle at 'a' is obtuse, 'a' is the closest point
    if dot(p - a, b - a) < 0:
        return abs(p - a)
    # If the angle at 'b' is obtuse, 'b' is the closest point
    if dot(p - b, a - b) < 0:
        return abs(p - b)
    # Otherwise, drop a perpendicular line to the segment
    return abs(cross(b - a, p - a)) / abs(b - a)

x1,y1,x2,y2,x3,y3=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j
p3=x3+y3*1j

print(f"{dist_pt_segment((p2,p3),p1):.6f}")