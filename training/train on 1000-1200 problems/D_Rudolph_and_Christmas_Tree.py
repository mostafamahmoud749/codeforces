import math

def areaTriangle(a,b,c):
    return abs(cross(b-a,c-a))/2

def areaPolygon(p):
    area=0.0
    for i in range(len(p)):
        area+=cross(p[i] , p[(i+1)%len(p)])
    
    return abs(area)/2

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

t=int(input())
for _ in range(t):
    n,d,h=map(int,input().split())
    points=list(map(int,input().split()))

    th=math.atan(h/(d/2))
    res=0

    for i in range(n-1):
        apt=d/2+points[i]*1j
        bpt=-(d/2)+points[i]*1j

        if points[i]+h <= points[i+1]:
            cpt=0+(points[i]+h)*1j
            
            res+=areaTriangle(apt,bpt,cpt)
        else:
            x=points[i+1]-points[i]
            y=x/math.tan(th)

            cpt=((d/2)-y)+(points[i]+x)*1j
            dpt=(-(d/2)+y)+(points[i]+x)*1j

            res+=areaPolygon([apt,bpt,dpt,cpt])
    
    res+=areaTriangle(d/2+points[-1]*1j,-d/2+points[-1]*1j,0+(points[-1]+h)*1j)


    print(f"{res:.6f}")