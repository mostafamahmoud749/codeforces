import math

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


def circle_circle_intersection_area(c1, r1, c2, r2):
    """
    Calculates the intersection area of two circles.
    - c1, c2: complex numbers representing the centers of the circles.
    - r1, r2: float radii of the circles.
    """
    d = abs(c2 - c1)
    if d >= r1 + r2:
        return 0.0
        
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2)**2
        
    theta1 = 2 * math.acos((r1**2 + d**2 - r2**2) / (2 * r1 * d))
    theta2 = 2 * math.acos((r2**2 + d**2 - r1**2) / (2 * r2 * d))
    
    area1 = 0.5 * r1**2 * (theta1 - math.sin(theta1))
    area2 = 0.5 * r2**2 * (theta2 - math.sin(theta2))
    
    return area1 + area2


t=int(input())
for _ in range(t):
    a,b,d=map(int,input().split())

    p1=a+(b+d/2)*1j
    p2=(a+d/2)+b*1j

    c1=a+b*1j
    c2=proj((p1,p2),c1)

    r1=d/2
    r2=d/(2*(2**.5))
    

    res=(math.pi*(r2**2))-circle_circle_intersection_area(c1,r1,c2,r2)

    print(f"{res*4:.6f}")

