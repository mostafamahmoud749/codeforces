import sys
import math

sys.stdin = open('bisector.in', 'r')
sys.stdout = open('bisector.out', 'w')

def perp_ccw(p):
    return p * 1j

def sgn(val, eps=1e-9):
    if val > eps:
        return 1
    if val < -eps:
        return -1
    return 0

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def proj(line, p):
    p1, p2 = line
    v = p2 - p1
    w = p - p1
    # Scale factor using dot product ratio: dot(w, v) / dot(v, v)
    # note: dot(v, v) is just the squared magnitude of v
    t = dot(w, v) / (v.real**2 + v.imag**2)
    return p1 + t * v

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def lines_intersection(line1, line2):
    a, b = line1
    c, d = line2
    
    # Check if lines are parallel using cross product of their directions
    cp = cross(b - a, d - c)
    if sgn(cp) == 0:
        return None  # Parallel or collinear (no unique intersection)
        
    # Using cross product ratio to find the intersection scalar along line1
    t = cross(c - a, d - c) / cp
    return a + t * (b - a)

def lines_bisector(line1, line2):
    # 1. Find where the two lines meet
    intersect_pt = lines_intersection(line1, line2)
    if intersect_pt is None:
        # If they are parallel, the bisector is the midway line parallel to both
        a, b = line1
        c, _ = line2
        mid_pt = (proj(line1, c) + c) / 2
        return (mid_pt, mid_pt + (b - a))
        
    # 2. Get unit direction vectors from the intersection point
    a, b = line1
    c, d = line2
    
    dir1 = b - a
    dir2 = d - c
    
    unit_dir1 = dir1 / abs(dir1)
    unit_dir2 = dir2 / abs(dir2)
    
    # 3. Add the unit vectors to get the bisector direction
    bisector_dir = unit_dir1 + unit_dir2
    
    # Edge case: If the lines point in exactly opposite directions, 
    # adding them gives 0. In that case, use the perpendicular vector.
    if abs(bisector_dir) < 1e-9:
        bisector_dir = perp_ccw(unit_dir1)
        
    return (intersect_pt, intersect_pt + bisector_dir)

def get_line_abc_float(line):
    p1, p2 = line
    A = p1.imag - p2.imag
    B = p2.real - p1.real
    C = -(A * p1.real + B * p1.imag)
        
    # Clean up floating point -0.0 issues
    if abs(A) < 1e-9: A = 0.0
    if abs(B) < 1e-9: B = 0.0
    if abs(C) < 1e-9: C = 0.0
    
    return A, B, C

x1,y1,x2,y2,x3,y3=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j
p3=x3+y3*1j

bi=lines_bisector((p1,p2),(p1,p3))
a,b,c=get_line_abc_float(bi)
print(f"{a:.6f} {b:.6f} {c:.6f}")