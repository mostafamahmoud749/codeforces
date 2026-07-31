import sys
import math

sys.stdin = open('angle2.in', 'r')
sys.stdout = open('angle2.out', 'w')


def angle(v, w):
    ang_v = math.atan2(v.imag, v.real)
    ang_w = math.atan2(w.imag, w.real)
    res = ang_w - ang_v
    while res > math.pi: res -= 2 * math.pi
    while res <= -math.pi: res += 2 * math.pi
    return abs(res)


x1,y1,x2,y2=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j


print(f"{angle(p1,p2):.6f}")