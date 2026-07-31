import math
from functools import cmp_to_key

################################# genral ##############################################

eps=1e-9

# save the point cord
A=3 + 4j

# gets the lenght from origin
abs(A)

# squared dist
def sq(p):
    return p.real**2 + p.imag**2

# check if a number is positive/negative/zero
def sgn(val, eps=1e-9):
    if val > eps:
        return 1
    if val < -eps:
        return -1
    return 0

# 5. Dot Product and Cross Product using complex numbers
def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    return a.real * b.imag - a.imag * b.real


############################## Transformation ##########################################

def scale_from_pivot(p, pivot, factor):
    return (p - pivot) * factor + pivot


def rotate_around_pivot(p, pivot, angle_rad):
    rotation_vector = complex(math.cos(angle_rad), math.sin(angle_rad))
    return (p - pivot) * rotation_vector + pivot

# if we have 2 points and there images and want to get the third image
def find_transformed_point(p1, p2, q1, q2, p3):
    ratio = (p3 - p1) / (p2 - p1)
    q3 = q1 + ratio * (q2 - q1)
    return q3


###################################### angles ##########################################

# absolute angle between two vectors $v$ and $w$
def angle(v, w):
    ang_v = math.atan2(v.imag, v.real)
    ang_w = math.atan2(w.imag, w.real)
    res = ang_w - ang_v
    while res > math.pi: res -= 2 * math.pi
    while res <= -math.pi: res += 2 * math.pi
    return abs(res)

def is_perp(v, w, eps=1e-9):
    return abs(dot(v, w)) < eps

def perp_ccw(p):
    """
    Returns the vector perpendicular to p, 
    rotated 90 degrees Counter-Clockwise.
    """
    return p * 1j  # Natively swaps (x, y) to (-y, x)


def perp_cw(p):
    """
    Returns the vector perpendicular to p, 
    rotated 90 degrees Clockwise.
    """
    return p * -1j

def orient(a,b,c):
    return sgn(cross(b-a,c-a))

def orientAngle(a, b, c):
    an=angle(b-a,c-a)
    if orient(a,b,c)>=0: return an
    return 2*math.pi-an

def angleTravelled(a, b, c):
    an=angle(b-a,c-a)
    if orient(a,b,c)>=0: return an
    return -an

def inAngle(a,b,c,p):
    abp=orient(a,b,p)
    acp=orient(a,c,p)
    abc=orient(a,b,c)

    if abc<0 : abp,acp=acp,abp

    return (abp>=0 and acp<=0) ^ (abc<0)


# Use Method 1 (atan2) for 95% of problems. It's concise, fast, and handles sorting across all 4 quadrants natively without extra code.
def polar_sort_atan2(points_list, origin=0+0j):
    """
    Sorts points counter-clockwise around an origin using math.atan2.
    """
    return sorted(
        points_list, 
        key=lambda p: math.atan2((p - origin).imag, (p - origin).real)
    )

# Use Method 2 (precise) only if coordinate values are massive integers or if the problem has tight constraints where values like 1e-9 will cause wrong answers.
def polar_sort_precise(points_list, origin=0+0j):
    """
    Sorts points counter-clockwise around an origin using integer cross-products.
    Completely immune to floating-point rounding bugs.
    """
    def compare(p1, p2):
        v1 = p1 - origin
        v2 = p2 - origin
        
        # Determine half-planes: 1 for upper-half, -1 for lower-half
        # This acts as the primary sort key (upper half-plane comes first)
        half1 = 1 if (v1.imag > 0 or (v1.imag == 0 and v1.real >= 0)) else -1
        half2 = 1 if (v2.imag > 0 or (v2.imag == 0 and v2.real >= 0)) else -1
        
        if half1 != half2:
            return -1 if half1 > half2 else 1
            
        # If they are in the same half-plane, use the cross product orientation
        # cross > 0 means v1 is clockwise from v2 (v2 is a left turn from v1)
        cp = cross(v1, v2)
        if sgn(cp) != 0:
            return -1 if cp > 0 else 1
            
        # Collinear fallback: sort by closer distance to the origin
        return -1 if abs(v1) < abs(v2) else 1

    return sorted(points_list, key=cmp_to_key(compare))

################################# line ############################

def side(line, p):
    p1, p2 = line
    return sgn(orient(p1, p2, p))

def dist_pt_line(line, p):
    p1, p2 = line
    # The magnitude of the cross product gives the area of the parallelogram
    area = abs(cross(p2 - p1, p - p1))
    line_len = abs(p2 - p1)
    return area / line_len

def perp_through(line, p):
    p1, p2 = line
    line_dir = p2 - p1
    # Rotate the line's direction vector by 90 degrees CCW to get the new direction
    perp_dir = perp_ccw(line_dir)
    # The new line starts at p and extends along the perpendicular direction
    return (p, p + perp_dir)

def sorting_along_line(line, points_list):
    p1, p2 = line
    line_dir = p2 - p1
    
    # Sort by the dot product scalar projection along the line direction
    # Use lambda to sort the original list in-place or return a sorted one
    return sorted(points_list, key=lambda p: dot(p - p1, line_dir))

def translate_by(line, v):
    p1, p2 = line
    # Shift both anchor points by the translation vector
    return (p1 + v, p2 + v)

def proj(line, p):
    p1, p2 = line
    v = p2 - p1
    w = p - p1
    # Scale factor using dot product ratio: dot(w, v) / dot(v, v)
    # note: dot(v, v) is just the squared magnitude of v
    t = dot(w, v) / (v.real**2 + v.imag**2)
    return p1 + t * v

def refl(line, p):
    # Reflection point = 2 * projection_point - original_point
    return 2 * proj(line, p) - p

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

#################### segmants ##############################

def inDisk(a,b,p):
    return dot(a-p,b-p) <= eps

def onSegment(a,b,c):
    return orient(a,b,c)==0 and inDisk(a,b,c)

def intersect_proper(seg1, seg2):
    a, b = seg1
    c, d = seg2
    # Check if a and b are on opposite sides of cd, AND c and d are on opposite sides of ab
    return (sgn(orient(c, d, a)) * sgn(orient(c, d, b)) < 0 and 
            sgn(orient(a, b, c)) * sgn(orient(a, b, d)) < 0)

def segments_intersect(seg1, seg2):
    a, b = seg1
    c, d = seg2
    if intersect_proper(seg1, seg2):
        return True
    # Check if any endpoint of one segment lies on the other segment
    return (onSegment(seg1, c) or onSegment(seg1, d) or 
            onSegment(seg2, a) or onSegment(seg2, b))


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