import sys
import math

sys.stdin = open('distance5.in', 'r')
sys.stdout = open('distance5.out', 'w')

eps=1e-6

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def sgn(val, eps=1e-6):
    if val > eps:
        return 1
    if val < -eps:
        return -1
    return 0

def orient(a,b,c):
    return sgn(cross(b-a,c-a))

def inDisk(a,b,p):
    return dot(a-p,b-p) <= eps

def onSegment(seg,c):
    a,b=seg
    return orient(a,b,c)==0 and inDisk(a,b,c)

# Checks if two finite segments cross cleanly forming an X-shape (excluding touching endpoints).
def intersect_proper(seg1, seg2):
    a, b = seg1
    c, d = seg2
    # Check if a and b are on opposite sides of cd, AND c and d are on opposite sides of ab
    return (sgn(orient(c, d, a)) * sgn(orient(c, d, b)) < 0 and 
            sgn(orient(a, b, c)) * sgn(orient(a, b, d)) < 0)


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

def segments_intersect(seg1, seg2):
    a, b = seg1
    c, d = seg2
    if intersect_proper(seg1, seg2):
        return True
    # Check if any endpoint of one segment lies on the other segment
    return (onSegment(seg1, c) or onSegment(seg1, d) or 
            onSegment(seg2, a) or onSegment(seg2, b))

def dist_segment_segment(seg1, seg2):
    if segments_intersect(seg1, seg2):
        return 0.0
        
    a, b = seg1
    c, d = seg2
    
    # Check all 4 endpoint-to-segment combinations
    return min(
        dist_pt_segment(seg2, a),
        dist_pt_segment(seg2, b),
        dist_pt_segment(seg1, c),
        dist_pt_segment(seg1, d)
    )





input_data = sys.stdin.read().split()


x1, y1, x2, y2 = map(int, input_data[0:4])
x3, y3, x4, y4 = map(int, input_data[4:8])


p1=x1+y1*1j
p2=x2+y2*1j
p3=x3+y3*1j
p4=x4+y4*1j

print(f"{dist_segment_segment((p1,p2),(p3,p4)):.6f}")