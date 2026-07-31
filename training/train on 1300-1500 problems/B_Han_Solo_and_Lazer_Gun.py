import math

def get_slope(p1, p2):

    diff = p2 - p1
    dy = int(diff.imag)
    dx = int(diff.real)
    
    if dx == 0 and dy == 0:
        return (0, 0)
        
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g

    if dx < 0 or (dx == 0 and dy < 0):
        dy = -dy
        dx = -dx
        
    return (dy, dx)

n,x0,y0=map(int,input().split())

st=set()
p1=x0+y0*1j

for i in range(n):
    x1,y1=map(int,input().split())
    p2=x1+y1*1j
    st.add(get_slope(p1,p2))

print(len(st))