import math
from functools import cmp_to_key

################################# genral ##############################################

eps=1e-9

# save the point cord
A=3 + 4j

# gets the lenght from origin
abs(A)

# Calculates the squared distance from the origin (avoids precision loss from sqrt).
def sq(p):
    return p.real**2 + p.imag**2

# Normalizes a float comparison: returns 1 if positive, -1 if negative, or 0 if within eps.
def sgn(val, eps=1e-9):
    if val > eps:
        return 1
    if val < -eps:
        return -1
    return 0

# Computes the vector dot product (useful for checking projection lengths and perpendicularity).
def dot(a, b):
    return a.real * b.real + a.imag * b.imag

# Computes the vector cross product (useful for area, orientation, and left/right turns).
def cross(a, b):
    return a.real * b.imag - a.imag * b.real


############################## Transformation ##########################################

# Scales point p toward or away from a given pivot point by a given factor.
def scale_from_pivot(p, pivot, factor):
    return (p - pivot) * factor + pivot


# Rotates point p counter-clockwise around a given pivot point by an angle in radians.
def rotate_around_pivot(p, pivot, angle_rad):
    rotation_vector = complex(math.cos(angle_rad), math.sin(angle_rad))
    return (p - pivot) * rotation_vector + pivot

# Predicts the new position of a third point p3 based on how p1 shifted to q1 and p2 to q2.
def find_transformed_point(p1, p2, q1, q2, p3):
    ratio = (p3 - p1) / (p2 - p1)
    q3 = q1 + ratio * (q2 - q1)
    return q3


###################################### angles ##########################################

# Returns the absolute smallest angle between two vectors v and w in radians (range 0 to pi).
def angle(v, w):
    ang_v = math.atan2(v.imag, v.real)
    ang_w = math.atan2(w.imag, w.real)
    res = ang_w - ang_v
    while res > math.pi: res -= 2 * math.pi
    while res <= -math.pi: res += 2 * math.pi
    return abs(res)

# Checks if two vectors v and w form a perfect 90-degree angle.
def is_perp(v, w, eps=1e-9):
    return abs(dot(v, w)) < eps

# Rotates vector p exactly 90 degrees counter-clockwise.
def perp_ccw(p):
    return p * 1j  # Natively swaps (x, y) to (-y, x)


# Rotates vector p exactly 90 degrees clockwise.
def perp_cw(p):
    return p * -1j

# Returns 1 if c is left of vector ab (CCW), -1 if right (CW), or 0 if on the same line.
def orient(a,b,c):
    return sgn(cross(b-a,c-a))

# Returns the counter-clockwise angle wrapped from a to b to c (range 0 to 2*pi).
def orientAngle(a, b, c):
    an=angle(b-a,c-a)
    if orient(a,b,c)>=0: return an
    return 2*math.pi-an

# Returns the directed angle from vector ab to ac (positive for CCW, negative for CW).
def angleTravelled(a, b, c):
    an=angle(b-a,c-a)
    if orient(a,b,c)>=0: return an
    return -an

# Checks if ray ap lies strictly inside the wedge angle formed between ray ab and ray ac.
def inAngle(a,b,c,p):
    abp=orient(a,b,p)
    acp=orient(a,c,p)
    abc=orient(a,b,c)

    if abc<0 : abp,acp=acp,abp

    return (abp>=0 and acp<=0) ^ (abc<0)


# Sorts points radially counter-clockwise around an origin using standard float angles.
def polar_sort_atan2(points_list, origin=0+0j):
    """
    Sorts points counter-clockwise around an origin using math.atan2.
    """
    return sorted(
        points_list, 
        key=lambda p: math.atan2((p - origin).imag, (p - origin).real)
    )

# Sorts points radially counter-clockwise around an origin using robust, cross-product integer math.
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

def point_along_direction(p, target, length):
    """
    Finds a point at a given distance (length) from point 'p' 
    moving directly towards 'target'.
    
    - p: complex (starting point, e.g., r + r*1j)
    - target: complex (direction target, e.g., 0 + 0j)
    - length: float (distance to travel, e.g., r)
    """
    # 1. Get the direction vector from p to target
    direction = target - p
    
    # Avoid division by zero if start and target are the same point
    dist = abs(direction)
    if dist < 1e-9:
        return p
        
    # 2. Normalize direction vector and scale it by length
    unit_dir = direction / dist
    
    # 3. Return the new point
    return p + unit_dir * length

# Returns 1 if point p is on the left side of directed line, -1 if on the right, or 0 if on it.
def side(line, p):
    p1, p2 = line
    return sgn(orient(p1, p2, p))

# Converts a line (p1, p2) into normalized float coefficients A, B, and C.
def get_line_abc_float(line):
    p1, p2 = line
    A = p1.imag - p2.imag
    B = p2.real - p1.real
    C = -(A * p1.real + B * p1.imag)
    
    # Normalize (A, B) to unit length
    norm = math.hypot(A, B)
    if norm > 1e-9:
        A /= norm
        B /= norm
        C /= norm
        
    # Clean up floating point -0.0 issues
    if abs(A) < 1e-9: A = 0.0
    if abs(B) < 1e-9: B = 0.0
    if abs(C) < 1e-9: C = 0.0
    
    return A, B, C

# Converts standard line coefficients A, B, and C back into a line tuple of two complex points (p1, p2).
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

# dis from point to a ray 
def dist_pt_ray(p, ray_start, ray_dir_pt):
    # If the projection is behind the start of the ray, the closest point is ray_start
    if dot(p - ray_start, ray_dir_pt - ray_start) < 0:
        return abs(p - ray_start)
    # Otherwise, return the standard perpendicular distance to the line
    return abs(cross(ray_dir_pt - ray_start, p - ray_start)) / abs(ray_dir_pt - ray_start)

# Finds the absolute perpendicular distance from a point p to an infinite line.
def dist_pt_line(line, p):
    p1, p2 = line
    # The magnitude of the cross product gives the area of the parallelogram
    area = abs(cross(p2 - p1, p - p1))
    line_len = abs(p2 - p1)
    return area / line_len

# Generates a new line that passes through point p and crosses the given line at a 90-degree angle.
def perp_through(line, p):
    p1, p2 = line
    line_dir = p2 - p1
    # Rotate the line's direction vector by 90 degrees CCW to get the new direction
    perp_dir = perp_ccw(line_dir)
    # The new line starts at p and extends along the perpendicular direction
    return (p, p + perp_dir)

# Sorts a list of points based on how far along the line direction they lie from line entry point p1.
def sorting_along_line(line, points_list):
    p1, p2 = line
    line_dir = p2 - p1
    
    # Sort by the dot product scalar projection along the line direction
    # Use lambda to sort the original list in-place or return a sorted one
    return sorted(points_list, key=lambda p: dot(p - p1, line_dir))

# Shifts the entire infinite line along a displacement vector v.
def translate_by(line, v):
    p1, p2 = line
    # Shift both anchor points by the translation vector
    return (p1 + v, p2 + v)

# Drops a perpendicular line from point p to find its closest coordinate projection on the line.
def proj(line, p):
    p1, p2 = line
    v = p2 - p1
    w = p - p1
    # Scale factor using dot product ratio: dot(w, v) / dot(v, v)
    # note: dot(v, v) is just the squared magnitude of v
    t = dot(w, v) / (v.real**2 + v.imag**2)
    return p1 + t * v

# Mirrors point p directly across the infinite line to its opposite side.
def refl(line, p):
    # Reflection point = 2 * projection_point - original_point
    return 2 * proj(line, p) - p

# Finds the exact unique crossing point of two infinite lines (returns None if they are parallel).
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

# Creates a line that splits the angle between line1 and line2 perfectly in half.
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

# Checks if point p is inside or on the border of a bounding circle defined by diameter ab.
def inDisk(a,b,p):
    return dot(a-p,b-p) <= eps

# Checks if point c lies exactly on the straight finite segment stretching between a and b.
def onSegment(a,b,c):
    return orient(a,b,c)==0 and inDisk(a,b,c)

# Checks if two finite segments cross cleanly forming an X-shape (excluding touching endpoints).
def intersect_proper(seg1, seg2):
    a, b = seg1
    c, d = seg2
    # Check if a and b are on opposite sides of cd, AND c and d are on opposite sides of ab
    return (sgn(orient(c, d, a)) * sgn(orient(c, d, b)) < 0 and 
            sgn(orient(a, b, c)) * sgn(orient(a, b, d)) < 0)

# Checks if two finite segments touch, cross, or overlap anywhere at all.
def segments_intersect(seg1, seg2):
    a, b = seg1
    c, d = seg2
    if intersect_proper(seg1, seg2):
        return True
    # Check if any endpoint of one segment lies on the other segment
    return (onSegment(seg1, c) or onSegment(seg1, d) or 
            onSegment(seg2, a) or onSegment(seg2, b))


# Computes the shortest distance from point p to a bounded finite segment (caps at endpoints).
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


# Finds the minimum distance separating two finite bounded segments (returns 0.0 if they touch/cross).
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

##################################### polygons ############################

def areaTriangle(a,b,c):
    return abs(cross(b-a,c-a))/2

def areaPolygon(p):
    area=0.0
    for i in range(len(p)):
        area+=cross(p[i] , p[(i+1)%len(p)])
    
    return abs(area)/2

# Helper to check if a point lies above or on the horizontal level of another point.
def above(a,p):
    return p.imag >= a.imag

# Helper to check if a horizontal ray starting at 'a' crosses the segment pq.
def crossesRay(a,p,q):
    return (above(a,q)-above(a,p)) * orient(a,p,q) > 0

# Checks if a point 'a' is strictly inside a polygon (odd number of ray crossings).
def inPolygon(polygon, a):
    crossings = 0
    n = len(polygon)
    for i in range(n):
        p = polygon[i]
        q = polygon[(i + 1) % n]
        if crossesRay(a, p, q):
            crossings += 1
    return crossings % 2 != 0


###################################### Circles ######################### 


def circle_line_intersection(c, r, line):
    p1, p2 = line
    p_proj = proj(line, c)
    d = abs(c - p_proj)
    
    if d > r + 1e-9:
        return []
    if abs(d - r) < 1e-9:
        return [p_proj]
        
    h = math.sqrt(max(0.0, r**2 - d**2))
    unit_dir = (p2 - p1) / abs(p2 - p1)
    return [p_proj + unit_dir * h, p_proj - unit_dir * h]


def circle_circle_intersection(c1, r1, c2, r2):
    d = abs(c2 - c1)
    
    if d > r1 + r2 + 1e-9 or d < abs(r1 - r2) - 1e-9 or d < 1e-9:
        return []

    if abs(d - (r1 + r2)) < 1e-9:
        unit_dir = (c2 - c1) / d
        return [c1 + unit_dir * r1]
    if abs(d - abs(r1 - r2)) < 1e-9:
        unit_dir = (c2 - c1) / d
        return [c1 + unit_dir * r1 if r1 > r2 else c1 - unit_dir * r1]
        
    # 3. Two intersection points
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0.0, r1**2 - a**2))
    
    unit_dir = (c2 - c1) / d
    mid_pt = c1 + unit_dir * a

    perp_dir = unit_dir * 1j * h
    
    return [mid_pt + perp_dir, mid_pt - perp_dir]


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

def circle_sector_area(r, angle, use_radians=True):
    """
    Calculates the area of a circle sector (pizza slice).
    - r: float (radius of the circle)
    - angle: float (the central angle of the slice)
    - use_radians: bool (True if angle is in radians, False if in degrees)
    """
    if use_radians:
        return 0.5 * (r**2) * angle
    else:
        return math.pi * (r**2) * (angle / 360.0)

def circle_area(r_or_p1, p2=None):
    """
    Calculates the total area of a circle.
    - Can be called with a single radius: circle_area(r)
    - Can be called with two complex points (center, boundary_point): circle_area(center, p)
    """
    if p2 is not None:
        r = abs(p2 - r_or_p1)
    else:
        r = r_or_p1
        
    return math.pi * (r**2)


def tangents_from_point_to_circle(p, c, r):
    """
    Finds the tangency points on a circle (center c, radius r) from an external point p.
    Returns: A list of 0, 1, or 2 complex numbers representing the points of tangency.
    """
    d = abs(c - p)
    
    # Point is inside the circle: no tangents possible
    if d < r - 1e-9:
        return []
        
    # Point is on the circle boundary: exactly 1 tangent (the perpendicular line at p)
    if abs(d - r) < 1e-9:
        return [p]
        
    # Point is outside the circle: 2 tangents
    h = math.sqrt(d**2 - r**2)
    
    # We find the intersection of the circle and a virtual circle centered at p with radius h
    # Using a simplified version of your circle-circle intersection math:
    a = (r**2 - h**2 + d**2) / (2 * d)
    height = math.sqrt(max(0.0, r**2 - a**2))
    
    unit_dir = (p - c) / d
    mid_pt = c + unit_dir * a
    perp_dir = unit_dir * 1j * height
    
    return [mid_pt + perp_dir, mid_pt - perp_dir]


def common_tangents_two_circles(c1, r1, c2, r2, outer=True):
    """
    Finds common tangent lines between Circle 1 (c1, r1) and Circle 2 (c2, r2).
    - outer: bool (if True, calculates the 2 outer tangents; if False, calculates the 2 inner tangents)
    
    Returns: A list of exactly 2 line tuples [(pt1, pt2), (pt1, pt2)] representing the 
    upper and lower tangents, or an empty list if they do not exist.
    """
    d = abs(c2 - c1)
    
    # Circles are concentric or too close to have well-defined separate tangents
    if d < 1e-9:
        return []

    # Choose signs based on whether we want outer or inner tangents
    # Outer: r1_sign = 1, r2_sign = -1
    # Inner: r1_sign = 1, r2_sign = 1
    r1_sign = 1
    r2_sign = -1 if outer else 1
    
    num = r1 * r1_sign + r2 * r2_sign
    if abs(num) > d + 1e-9:
        return []  # No tangents possible (e.g., circles overlap too much for inner tangents)
        
    cos_alpha = num / d
    cos_alpha = max(-1.0, min(1.0, cos_alpha))  # Floating point clamping
    sin_alpha = math.sqrt(max(0.0, 1.0 - cos_alpha**2))
    
    unit_dir = (c2 - c1) / d
    tangents = []
    
    # Sign 1 (+1) represents the "upper" tangent (CCW rotation)
    # Sign -1 (-1) represents the "lower" tangent (CW rotation)
    for sign in [1, -1]:
        # Rotate the base vector to get normal directions
        rot = cos_alpha + sign * sin_alpha * 1j
        
        # Normal directions pointing to the tangent contact points on each circle boundary
        n1 = unit_dir * rot * r1_sign
        n2 = unit_dir * rot * (-r2_sign)
        
        p1 = c1 + n1 * r1
        p2 = c2 + n2 * r2
        tangents.append((p1, p2))
        
    return tangents