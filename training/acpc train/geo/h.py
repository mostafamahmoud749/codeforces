import sys
import math

sys.stdin = open('distance3.in', 'r')
sys.stdout = open('distance3.out', 'w')

def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def dist_pt_ray(p, ray_start, ray_dir_pt):
    # If the projection is behind the start of the ray, the closest point is ray_start
    if dot(p - ray_start, ray_dir_pt - ray_start) < 0:
        return abs(p - ray_start)
    # Otherwise, return the standard perpendicular distance to the line
    return abs(cross(ray_dir_pt - ray_start, p - ray_start)) / abs(ray_dir_pt - ray_start)

x1,y1,x2,y2,x3,y3=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j
p3=x3+y3*1j

line=(p2,p3)

print(f"{dist_pt_ray(p1,p2,p3):.6f}")