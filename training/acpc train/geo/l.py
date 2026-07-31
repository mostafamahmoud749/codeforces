import sys
import math

sys.stdin = open('length.in', 'r')
sys.stdout = open('length.out', 'w')


x1,y1,x2,y2=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j


print(f"{abs(p1-p2):.6f}")