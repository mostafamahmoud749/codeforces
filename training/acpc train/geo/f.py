import sys
import math

sys.stdin = open('distance1.in', 'r')
sys.stdout = open('distance1.out', 'w')


def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def line_from_abc(A, B, C):
    # The direction vector of the line is perpendicular to the normal vector (A, B)
    direction = -B + A * 1j
    
    # Find a starting point p1 by setting one coordinate to 0 (safely choosing the larger coefficient)
    if abs(A) > abs(B):
        # Set y = 0 -> Ax + C = 0 -> x = -C/A
        p1 = (-C / A) + 0j
    else:
        # Set x = 0 -> By + C = 0 -> y = -C/B
        p1 = 0 + (-C / B) * 1j
        
    return (p1, p1 + direction)

def proj(line, p):
    p1, p2 = line
    v = p2 - p1
    w = p - p1
    # Scale factor using dot product ratio: dot(w, v) / dot(v, v)
    # note: dot(v, v) is just the squared magnitude of v
    t = dot(w, v) / (v.real**2 + v.imag**2)
    return p1 + t * v

x1,y1,a,b,c=map(int,input().split())

p=x1+y1*1j
line=(line_from_abc(a,b,c))


print(f"{abs(p-proj(line,p)):.6f}")
