import math

def get_circumcircle_area(v, s):
    """
    Calculates the area of the smallest circle that contains 
    the regular polygon (the circumcircle).
    """
    h = s / (2.0 * math.sin(math.pi / v))
    return math.pi * (h ** 2)

v,s=map(int,input().split())

res=get_circumcircle_area(v,s)
print(f"{res:.6f}")