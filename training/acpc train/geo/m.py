import sys
import math

sys.stdin = open('line1.in', 'r')
sys.stdout = open('line1.out', 'w')

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


x1,y1,x2,y2=map(int,input().split())

p1=x1+y1*1j
p2=x2+y2*1j

a,b,c=get_line_abc_float((p2,p1))

print(a,b,c)